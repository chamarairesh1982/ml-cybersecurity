# Cybersecurity ML: evidence journal

## Section 1 — phishing email triage

The notebook implements a complete learning experiment using the versioned public corpus in DATASET_SELECTION.md, loaded directly in Colab. The question is whether message text supports analyst triage while limiting false alerts. Real-data results are pending execution.

### Preparation

Audit types, missing values, labels and lengths without displaying email bodies. Remove missing/empty/sentinel records, normalise text, exclude contradictory duplicates and deduplicate consistent copies. Report character truncation. Group template fingerprints and verified near-duplicate shingles before a fixed grouped split. Content groups are imperfect proxies for campaigns.

Training-only EDA informs understanding. Fit vocabulary, TF-IDF and numerical scaling within training boundaries or CV folds. Compare word TF-IDF, word+character features and a stopword/stemming ablation. Structural features capture counts and character ratios.

### Models and validation

Compare prior, regularised logistic regression, linear SVM, structural logistic regression and random forest. Tune bounded grids on identical grouped training CV folds using average precision. SVM margins are ranking scores, not calibrated probabilities.

The neural comparator learns embeddings and uses padding-aware average pooling and dense layers. It does not model word order. Use regularisation, dropout, class weights, validation early stopping and two fixed seeds. Vectorise strings on CPU before numerical GPU/TPU training.

Validation selects thresholds and the winner by recall under an illustrative 1% legitimate-message false-positive budget, then AP and fitting cost. This is an empirical budget, not a population guarantee. Do not refit on validation after choosing thresholds.

### Final evidence

Evaluate the untouched test once. Record accuracy, precision, recall, F1, AP, ROC-AUC, FPR, false alerts per 1,000 legitimate messages, confusion counts and runtime. Plot PR/ROC curves and the winner's confusion matrix. Retain the validation-selected winner. Report group-bootstrap intervals and aggregate errors by length/class.

**Real-data outcomes: pending Colab execution.** Do not assume deep learning wins. Further development after examining test results needs a new independent holdout.

Label quality, historical/source artefacts, approximate grouping, truncation and absent time/source metadata limit generalisation. Neural seed variation does not measure deployment shift. Independent data and operational monitoring would be required for practical use.

## Section 2 — network intrusion classification

The self-contained notebook classifies ten provider-labelled flow categories using a pinned parquet mirror of the UNSW-NB15 published train/test partitions. Fetching occurs in Colab memory. The test partition remains unfetched until validation decisions freeze. No reliable chronology or session metadata are established by this reformatted artifact.

Audit schema, label consistency, invalid/missing numeric values and duplicates. Exclude row IDs, both target fields and TCP initial sequence numbers from predictors. Remove conflicting feature-identical labels and consistent duplicate copies. Group rounded core measurements plus categorical fields so identical core-ablation inputs cannot cross partitions. Reserve fixed grouped validation data from the training partition and use grouped CV within training only.

Create row-local flow ratios; fit median imputation, log transforms, one-hot encoding and any scaling inside training boundaries. Compare prior, logistic regression, random forest, histogram gradient boosting, and a boosted core-feature ablation excluding TTL/context counts. The numerical MLP uses regularisation, dropout, weighted training, validation early stopping and two fixed seeds; GPU/TPU execution still needs actual runtime verification.

Validation macro-F1 selects the category classifier. A separate attack-score threshold maximises validation recall under an illustrative 1% Normal false-alert budget. Keep category argmax decisions separate from binary alerts; model probabilities are not assumed calibrated.

Final testing removes exact and rounded-group overlap with all development data and reports exclusions/class support. Scores therefore describe a novelty subset rather than the original row-weighted benchmark. Report fixed-taxonomy macro/per-class precision, recall and F1, confusion/PR curves, defined-class OVR AP/ROC-AUC, alert recall/FPR/workload, runtime, group-bootstrap intervals and aggregate protocol errors. Retain the validation-selected winner regardless of test rankings.

**Real-data outcomes: pending Colab execution.** Historical synthetic attacks, label quality, feature timing, contextual collection shortcuts and approximate grouping limit deployment inference. Further tuning after test inspection requires a new independent holdout.

## Remaining scenarios

Sections 3 (anomaly) and 4 (ransomware) retain reserved notebooks. Implement them when requested; no implementation or results are claimed for them.
