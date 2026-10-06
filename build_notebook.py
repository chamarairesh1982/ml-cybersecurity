"""Build the anonymous, output-free learning notebook."""
import json
from pathlib import Path

ROOT = Path(__file__).parent
cells = []

def md(text):
    cells.append(dict(cell_type='markdown', metadata={}, source=text.strip().splitlines(True)))

def code(text):
    cells.append(dict(cell_type='code', metadata={}, source=text.strip().splitlines(True), execution_count=None, outputs=[]))

md('''# COMP70049-Assignment_2026
## Machine learning for cybersecurity: independent learning project
No author name, student number, email address, or private data is included.
This notebook uses four cybersecurity topics as a learning roadmap rather than a submission checklist.
No dataset is bundled or downloaded automatically. No measured results are claimed.

**Work order:** complete Section 1, review its evidence, then implement Sections 2, 3, and 4.
Section 1 contains executable training code that requires your own authorised, labelled CSV.
Sections 2–4 currently contain experiment designs, not trained models.

### Learning foundations
Data preparation and EDA → feature engineering → supervised learning → neural networks →
ensemble methods → evaluation → unsupervised learning → deep learning and NLP.

### Evidence standard
Define the prediction target, investigate label quality, split before fitting transformations,
compare against a simple baseline, select models on validation data, and evaluate a held-out test once.
There is no universally best model: the useful choice depends on data quality, deployment shift,
false-positive cost, detection benefit, and computation.''')
md('''# Section 1 — Email security and phishing detection
## 1.1 Research question and scope
Can email text distinguish provider-labelled phishing from legitimate messages, and does a
sequence model improve the quality enough to justify its additional cost?
Spam and phishing are different targets. A spam label alone cannot establish phishing detection.
This experiment is text-based screening; it does not inspect attachments or establish that a message is safe.

## 1.2 Dataset contract
Prepare a UTF-8 CSV locally with `text` and `label`: 0 = legitimate, 1 = phishing.
Use only data you are authorised to process. Remove direct personal identifiers before loading.
An optional `group` column should identify related messages, campaigns, or sources.
The notebook does not upload to GitHub or save raw messages in outputs.
Document provenance, licence, collection period, label method, and sampling limitations separately.
Do not choose a dataset merely because it produces high accuracy.

## 1.3 Experiment configuration
CPU supports the baseline. The optional LSTM needs TensorFlow and may benefit from a Colab GPU.
Run cells in order. Keep the final test evaluation cell for the end of the experiment.''')
code('''import importlib.metadata as metadata
import random
import time
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GroupShuffleSplit
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (average_precision_score, roc_auc_score, precision_score,
    recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay,
    PrecisionRecallDisplay, RocCurveDisplay, precision_recall_curve)

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
DATA_PATH = Path('/content/email_data.csv')  # Change for your own local CSV.
TEXT_COLUMN = 'text'
LABEL_COLUMN = 'label'
GROUP_COLUMN = 'group'  # Used only when present; never used as a predictor.
RUN_LSTM = False       # Enable only after the classical workflow succeeds.
MIN_PHISHING_RECALL = 0.90  # Illustrative learning target, not a deployment guarantee.
for package in ['numpy', 'pandas', 'scikit-learn', 'matplotlib']:
    print(package, metadata.version(package))''')
md('''## 1.4 Audit and conservative cleaning
The audit displays counts, not raw message text. Normalise whitespace and remove exact text
duplicates. Exclude identical texts with contradictory labels and report the exclusions.
This does not remove near duplicates: use campaign/group identifiers or a separate similarity
audit when available. Avoid automatically stripping URLs, punctuation, or negation because
these may carry useful signals. Compare stronger cleaning only as a validation experiment.''')
code('''if not DATA_PATH.is_file():
    raise FileNotFoundError('Provide your authorised email CSV and update DATA_PATH. No dataset is bundled.')
df = pd.read_csv(DATA_PATH)
required = {TEXT_COLUMN, LABEL_COLUMN}
if not required.issubset(df.columns):
    raise ValueError('CSV must contain the configured text and label columns.')
original_n = len(df)
df = df.dropna(subset=[TEXT_COLUMN, LABEL_COLUMN]).copy()
if not df[LABEL_COLUMN].isin([0, 1]).all():
    raise ValueError('Labels must be numeric 0 (legitimate) or 1 (phishing).')
df[LABEL_COLUMN] = df[LABEL_COLUMN].astype(int)
df[TEXT_COLUMN] = df[TEXT_COLUMN].astype(str).str.replace(r'\\s+', ' ', regex=True).str.strip()
df = df.loc[df[TEXT_COLUMN].str.len() > 0].copy()
normalised = df[TEXT_COLUMN].str.casefold()
conflict_keys = df.assign(_key=normalised).groupby('_key')[LABEL_COLUMN].nunique()
conflicts = normalised.isin(conflict_keys[conflict_keys > 1].index)
conflict_n = int(conflicts.sum())
df = df.loc[~conflicts].copy()
df = df.loc[~df[TEXT_COLUMN].str.casefold().duplicated()].reset_index(drop=True)
if df[LABEL_COLUMN].nunique() != 2 or df[LABEL_COLUMN].value_counts().min() < 20:
    raise ValueError('This learning workflow requires at least 20 examples in each class after cleaning.')
print({'original_rows': original_n, 'retained_rows': len(df), 'conflicting_rows_excluded': conflict_n})
print('Class counts:', df[LABEL_COLUMN].value_counts().sort_index().to_dict())
df[TEXT_COLUMN].str.len().hist(bins=40)
plt.xlabel('Message length in characters'); plt.ylabel('Count'); plt.title('Length audit'); plt.show()''')
md('''## 1.5 Train / validation / test split
Use about 70/15/15. If `group` exists, related examples stay together, though group sizes
can change these proportions. Without groups, a stratified random split is only an initial
learning experiment and may overestimate generalisation. A chronological or independent
source holdout is stronger evidence for future messages. Do not repeatedly search splits for a high score.''')
code('''indices = np.arange(len(df))
if GROUP_COLUMN in df.columns:
    if df[GROUP_COLUMN].isna().any():
        raise ValueError('Group identifiers must be complete when using group splits.')
    groups = df[GROUP_COLUMN].astype(str).to_numpy()
    if len(np.unique(groups)) < 7:
        raise ValueError('Provide at least seven distinct groups, or design an explicit source holdout.')
    split = GroupShuffleSplit(n_splits=1, test_size=0.30, random_state=SEED)
    train_i, remaining_i = next(split.split(indices, df[LABEL_COLUMN], groups))
    split2 = GroupShuffleSplit(n_splits=1, test_size=0.50, random_state=SEED + 1)
    val_local, test_local = next(split2.split(remaining_i, groups=groups[remaining_i]))
    val_i, test_i = remaining_i[val_local], remaining_i[test_local]
    assert not (set(groups[train_i]) & set(groups[val_i]))
    assert not (set(groups[train_i]) & set(groups[test_i]))
    assert not (set(groups[val_i]) & set(groups[test_i]))
else:
    train_i, remaining_i = train_test_split(indices, test_size=0.30, stratify=df[LABEL_COLUMN], random_state=SEED)
    val_i, test_i = train_test_split(remaining_i, test_size=0.50,
        stratify=df.iloc[remaining_i][LABEL_COLUMN], random_state=SEED)
parts = {}
for name, idx in [('train', train_i), ('validation', val_i), ('test', test_i)]:
    part = df.iloc[idx]
    if part[LABEL_COLUMN].nunique() != 2:
        raise ValueError(f'{name} lacks a class. Design a defensible grouped split before training.')
    parts[name] = (part[TEXT_COLUMN].to_numpy(), part[LABEL_COLUMN].to_numpy())
    print(name, len(idx), 'class counts:', part[LABEL_COLUMN].value_counts().sort_index().to_dict())
X_train, y_train = parts['train']
X_val, y_val = parts['validation']
X_test, y_test = parts['test']''')
md('''## 1.6 Baseline and classical model
Compare a prior-probability baseline with word TF-IDF logistic regression. TF-IDF is fitted
only on training text. Select regularisation on validation average precision (AP).
AP is a ranking summary of the precision–recall curve; it is not the same as trapezoidal PR-AUC.
Class weighting is a starting choice, not a substitute for examining prevalence and error cost.''')
code('''models, fit_seconds, validation_rows = {}, {}, []
baseline = DummyClassifier(strategy='prior').fit(np.zeros((len(y_train), 1)), y_train)
models['Prior baseline'] = baseline
fit_seconds['Prior baseline'] = 0.0
for c in [0.1, 1.0, 10.0]:
    model = Pipeline([
        ('tfidf', TfidfVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1,
            max_features=50000, sublinear_tf=True)),
        ('classifier', LogisticRegression(C=c, class_weight='balanced', max_iter=1000, random_state=SEED))])
    start = time.perf_counter()
    model.fit(X_train, y_train)
    duration = time.perf_counter() - start
    scores = model.predict_proba(X_val)[:, 1]
    validation_rows.append({'C': c, 'validation_AP': average_precision_score(y_val, scores),
                            'fit_seconds': duration})
    models[f'LR C={c}'] = model
    fit_seconds[f'LR C={c}'] = duration
validation_table = pd.DataFrame(validation_rows).sort_values('validation_AP', ascending=False)
print(validation_table.to_string(index=False))
best_c = float(validation_table.iloc[0]['C'])
selected = {'Prior baseline': baseline, 'TF-IDF Logistic Regression': models[f'LR C={best_c}']}
selected_times = {'Prior baseline': 0.0, 'TF-IDF Logistic Regression': fit_seconds[f'LR C={best_c}']}''')
md('''## 1.7 Optional deep learning comparison
An embedding + bidirectional LSTM is a learning comparator, not an assumed improvement.
Vocabulary adaptation and network fitting use training text only. Validation loss selects the epoch.
The 300-token truncation and 20,000-token vocabulary are starting settings: measure truncation
and tune within a fixed validation budget. Run several seeds before drawing conclusions about small differences.
Enable `RUN_LSTM` in the configuration cell and rerun the workflow to include this model.''')
code('''if RUN_LSTM:
    import tensorflow as tf
    tf.keras.utils.set_random_seed(SEED)
    print('tensorflow', tf.__version__)
    vectorise = tf.keras.layers.TextVectorization(max_tokens=20000, output_sequence_length=300)
    vectorise.adapt(tf.data.Dataset.from_tensor_slices(X_train).batch(64))
    deep = tf.keras.Sequential([
        tf.keras.Input(shape=(), dtype=tf.string), vectorise,
        tf.keras.layers.Embedding(20000, 64, mask_zero=True),
        tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(32)),
        tf.keras.layers.Dropout(0.3), tf.keras.layers.Dense(1, activation='sigmoid')])
    deep.compile(optimizer='adam', loss='binary_crossentropy')
    train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(len(y_train), seed=SEED).batch(64)
    val_ds = tf.data.Dataset.from_tensor_slices((X_val, y_val)).batch(64)
    weights = {int(k): len(y_train)/(2*int(v)) for k, v in zip(*np.unique(y_train, return_counts=True))}
    start = time.perf_counter()
    history = deep.fit(train_ds, validation_data=val_ds, epochs=10, class_weight=weights,
        callbacks=[tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)])
    selected_times['BiLSTM'] = time.perf_counter() - start
    selected['BiLSTM'] = deep
    pd.DataFrame(history.history)[['loss', 'val_loss']].plot(title='LSTM learning curves')
    plt.xlabel('Epoch index'); plt.ylabel('Binary cross-entropy'); plt.show()
else:
    print('LSTM disabled: no deep learning result has been produced.')''')
md('''## 1.8 Select operating thresholds using validation only
For each trained classifier, find the threshold with the highest precision among candidates
that reach the illustrative recall target. This is a learning policy; it does not guarantee
that production recall will meet the target. Report test false-positive rates as well as recall.
Keep a threshold of 0.5 for the constant-score baseline.''')
code('''def probability(model, name, texts):
    if name == 'Prior baseline':
        return model.predict_proba(np.zeros((len(texts), 1)))[:, 1]
    if name == 'BiLSTM':
        return model.predict(tf.data.Dataset.from_tensor_slices(texts).batch(64), verbose=0).ravel()
    return model.predict_proba(texts)[:, 1]

thresholds = {}
for name, model in selected.items():
    scores = probability(model, name, X_val)
    if name == 'Prior baseline':
        thresholds[name] = 0.5
        continue
    precisions, recalls, candidates = precision_recall_curve(y_val, scores)
    feasible = np.flatnonzero(recalls[:-1] >= MIN_PHISHING_RECALL)
    best = max(feasible, key=lambda i: (precisions[i], candidates[i]))
    thresholds[name] = float(candidates[best])
print('Validation-selected thresholds:', thresholds)''')
md('''## 1.9 Final held-out evaluation — run after decisions are frozen
These results describe this test partition only. AP and ROC-AUC use continuous scores;
precision, recall, F1, and false-positive rate use the validation-selected threshold.
Do not adjust the model or threshold after inspecting these results; use new independent data
for a subsequent experiment. Never paste raw email examples into a public report.''')
code('''if globals().get('_final_test_evaluated', False):
    raise RuntimeError('Test already evaluated in this session. Keep it held out during model development.')
results = []
for name, model in selected.items():
    start = time.perf_counter()
    scores = probability(model, name, X_test)
    elapsed = time.perf_counter() - start
    predictions = (scores >= thresholds[name]).astype(int)
    tn, fp, fn, tp = confusion_matrix(y_test, predictions, labels=[0, 1]).ravel()
    results.append({'model': name, 'threshold': thresholds[name],
        'precision': precision_score(y_test, predictions, zero_division=0),
        'recall': recall_score(y_test, predictions, zero_division=0),
        'F1': f1_score(y_test, predictions, zero_division=0),
        'AP': average_precision_score(y_test, scores), 'ROC_AUC': roc_auc_score(y_test, scores),
        'FPR': fp/(fp+tn), 'TN': int(tn), 'FP': int(fp), 'FN': int(fn), 'TP': int(tp),
        'fit_seconds': selected_times[name], 'test_seconds': elapsed})
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    ConfusionMatrixDisplay.from_predictions(y_test, predictions, display_labels=['Legitimate', 'Phishing'], ax=axes[0])
    PrecisionRecallDisplay.from_predictions(y_test, scores, ax=axes[1])
    RocCurveDisplay.from_predictions(y_test, scores, ax=axes[2])
    fig.suptitle(name); plt.tight_layout(); plt.show()
results_table = pd.DataFrame(results)
print(results_table.to_string(index=False))
_final_test_evaluated = True''')
md('''## 1.10 Write the evidence-based discussion
Before experiments: all outcomes are **pending**. After experiments, report class counts,
split policy, cleaning exclusions, selected settings, threshold, metrics, runtime, and error tradeoffs.
Explain whether extra complexity improved AP or useful operating-point performance.
Discuss near-duplicate leakage, source artefacts, changing attack language, label noise,
prevalence shift, and incomplete text. Use bootstrap confidence intervals or repeated training
seeds for uncertainty; do not describe a small single-run difference as definitive.

**Checkpoint before Section 2:** verify provenance and licence; review partition independence;
run a stronger source/time holdout; decide whether the LSTM comparison is useful;
write conclusions supported by actual measurements.''')
md('''# Section 2 — Network intrusion classification
**Status: experiment design; implementation follows the Section 1 checkpoint.**

Research question: can flow features distinguish attack categories on previously unseen capture periods?
Dataset contract: labelled flow table with documented capture days, protocols, attack taxonomy,
and an independent split. Keep raw IPs, identifiers, timestamps, and collection artefacts out of
predictors unless justified by the prediction task. No dataset is selected or bundled.

1. Audit class prevalence, missing/infinite values, duplicated flows, and label definitions.
2. Split by capture day/session before learning imputers, encoders, scaling, or feature selection.
3. Compare a prior baseline, random forest, and a small dense neural network. A CNN requires
   a defensible local structure; arbitrary tabular column order does not justify convolution.
4. Select settings using validation macro-F1 and inspect rare-class recall.
5. Report macro-F1, per-class precision/recall, confusion matrix, one-vs-rest AP, runtime,
   and performance on unseen capture days. Accuracy alone can hide minority-class failure.
6. Discuss source-specific artefacts, changing traffic, and false alerts per traffic volume.''')
md('''# Section 3 — Anomaly detection for cyber threats
**Status: experiment design; implementation follows Section 2.**

Research question: do models trained on verified normal traffic detect unusual future activity
within a stated false-positive budget? Unusual does not automatically mean malicious.
Dataset contract: numerical/categorical traffic features, timestamps or sessions for splitting,
and labels reserved for audit and evaluation. No dataset is selected or bundled.

1. Use capture/session holdouts and fit preprocessing on training normal traffic only.
2. State whether training data are verified normal or potentially contaminated.
3. Compare Isolation Forest, a simple distance baseline, and an autoencoder.
4. Fit autoencoder scaling on training data and use held-out normal traffic for stopping.
5. Select thresholds from normal validation scores using a declared false-positive budget.
   If attack labels select thresholds, describe the approach as supervised calibration.
6. Test once on normal and attack traffic; report recall/TPR, FPR, AP, and missed attack types.
7. Assess changing normal behaviour and alert workload. An anomaly score alone does not
   prove zero-day detection.''')
md('''# Section 4 — Ransomware behaviour screening
**Status: experiment design; implementation follows Section 3.**

Research question: can observed API/event sequences flag suspicious processes early enough
to support investigation? Detection performance does not establish prevention effectiveness.
Dataset contract: authorised benign/ransomware event sequences with process/sample IDs,
families, collection environment, and time order. Use recorded features only; no malware
execution, binaries, or live system changes are part of this learning project.

1. Audit sequence provenance, family balance, duplicates, and observation duration.
2. Split by sample/process and hold out ransomware families or collection environments.
3. Compare gradient boosting on event-count features with an embedding LSTM on ordered events.
4. Fit vocabulary and padding/truncation rules on training sequences; measure lost sequence coverage.
5. Select hyperparameters and thresholds on validation data; test once on the family holdout.
6. Report precision, recall, F1, AP, benign FPR, runtime, and performance at early observation windows.
7. Discuss collection artefacts, unseen families, event loss, and operational response requirements.
   If only static file features are available, rename the task static screening and choose models
   appropriate to those features rather than claiming behaviour over time.''')
md('''# Learning report and next steps
Use `REPORT.md` as the report companion. Its current content explains methodology and
pending evidence. Add measured results only after selecting an authorised dataset and running
the experiment. Keep datasets, trained models, local paths, private examples, and notebook
outputs out of public Git commits. Section-by-section review is the intended workflow.''')
notebook = dict(cells=cells, metadata={'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
    'language_info': {'name': 'python'}, 'colab': {'name': 'COMP70049-Assignment_2026.ipynb'}}, nbformat=4, nbformat_minor=5)
for i, cell in enumerate(cells):
    cell['id'] = f'learning-{i:03d}'
(ROOT / 'COMP70049-Assignment_2026.ipynb').write_text(json.dumps(notebook, indent=2, ensure_ascii=False), encoding='utf-8')
print(f'Created notebook with {len(cells)} cells; all outputs cleared.')
