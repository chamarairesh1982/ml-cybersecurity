# Machine learning for cybersecurity: learning report

## Purpose and current evidence

This independent project studies four cybersecurity prediction problems. Its purpose is to develop experimental judgement: connect data quality, feature design, model choice, and evaluation to useful security decisions. It is organised as a learning report rather than a completed assignment submission.

No dataset has been selected, no model has been trained on real data in this project, and no performance claim is made. Section 1 has executable code. Sections 2–4 are planned experiments. A final comparative report requires measured evidence from all four sections.

## Shared methodology

Define what each label means and how it was obtained. Audit missing values, duplicates, class imbalance, collection artefacts, and privacy. Split related samples together before fitting learned transformations. Reserve validation data for model and threshold selection and keep the test partition untouched until decisions are frozen. Prefer temporal, source, session, or family holdouts when they match the intended generalisation question.

Compare a simple baseline with a classical model and, when appropriate, a deep model. Model complexity is justified by stronger evidence or useful operational benefit, not by its name. Record runtime, software versions, seeds, split policy, and selected settings. Evaluate performance under plausible shift and discuss label limitations. Report uncertainty before interpreting small differences.

## 1. Email phishing detection

The proposed target is provider-labelled phishing versus legitimate email text. A spam dataset does not automatically provide phishing labels. The notebook checks labels, removes empty texts and exact normalised duplicates, and excludes contradictory duplicates. It preserves potentially useful punctuation and link tokens instead of applying every cleaning technique automatically.

TF-IDF logistic regression provides an interpretable, efficient text baseline. A prior classifier identifies the benefit over class prevalence alone. An optional embedding BiLSTM explores sequential information. Vocabulary, TF-IDF weights, and model parameters are learned only from training data. Validation average precision selects logistic regularisation; validation loss selects the LSTM epoch. Validation data also select an illustrative recall-oriented operating threshold.

Held-out evaluation includes precision, recall, F1, average precision, ROC-AUC, confusion counts, false-positive rate, and runtime. Precision–recall performance is particularly useful when phishing is rare. Group-aware splitting helps keep related examples together, but random splitting without campaign identifiers remains vulnerable to near-duplicate and source leakage. External or chronological validation is needed before suggesting practical usefulness.

**Results and conclusion: pending authorised dataset selection and execution.** Compare observed scores, operating-point errors, training cost, and shift sensitivity before recommending a model. No claim that the LSTM is better is justified yet.

## 2. Network intrusion classification

The planned task predicts attack categories from flow features. Capture days and sessions should define partitions; collection identifiers can create misleading shortcuts. Imputation, encoding, scaling, and feature selection must be fitted inside training boundaries. Compare random forest with a dense neural network and a prior baseline. Use macro-F1, per-class recall and precision, confusion matrices, and one-vs-rest average precision. A CNN is appropriate only if the input representation has meaningful local structure. Assess unseen capture days and rare attacks before interpreting overall accuracy.

**Dataset, implementation, results, and conclusion: pending.**

## 3. Anomaly detection

The planned task learns normal traffic and scores departures from it. Compare Isolation Forest, a distance baseline, and an autoencoder. Distinguish verified-normal training from contaminated training. Use normal validation data to set a false-positive budget; calibration using attack labels changes the interpretation of the experiment. Evaluate on an independent labelled test partition with AP, TPR/recall, FPR, and attack-specific detection. Anomaly detection identifies unusual observations; confirming maliciousness requires additional evidence.

**Dataset, implementation, results, and conclusion: pending.**

## 4. Ransomware behaviour screening

The planned task uses recorded API/event sequences, comparing gradient boosting on count features with an LSTM on ordered events. Keep events from the same process or sample in one partition and hold out families or environments. Evaluate early observation windows as well as full sequences. Report benign FPR, precision, recall, F1, AP, and runtime. Static headers would support a different static-screening question. Neither static nor behavioural classification alone proves prevention of damage.

**Dataset, implementation, results, and conclusion: pending.**

## Evidence to add after each experiment

Record dataset provenance and licence, sample/class counts, collection period, label quality, exclusions, split independence, feature policy, model settings, validation decisions, held-out metrics, figures, runtime, uncertainty, and limitations. Do not publish raw examples containing personal information. A final recommendation should state the observed benefit, cost, and conditions under which the conclusion could fail.
