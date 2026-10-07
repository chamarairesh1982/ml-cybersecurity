# Cybersecurity ML: evidence journal

## Section 1 — phishing email triage

The notebook implements a complete learning experiment using the versioned public corpus in DATASET_SELECTION.md, loaded directly in Colab. The question is whether message text supports analyst triage while limiting false alerts. The saved Colab run has been reviewed below.

### Preparation

Audit types, missing values, labels and lengths without displaying email bodies. Remove missing/empty/sentinel records, normalise text, exclude contradictory duplicates and deduplicate consistent copies. Report character truncation. Group template fingerprints and verified near-duplicate shingles before a fixed grouped split. Content groups are imperfect proxies for campaigns.

Training-only EDA informs understanding. Fit vocabulary, TF-IDF and numerical scaling within training boundaries or CV folds. Compare word TF-IDF, word+character features and a stopword/stemming ablation. Structural features capture counts and character ratios.

### Models and validation

Compare prior, regularised logistic regression, linear SVM, structural logistic regression and random forest. Tune bounded grids on identical grouped training CV folds using average precision. SVM margins are ranking scores, not calibrated probabilities.

The neural comparator learns embeddings and uses padding-aware average pooling and dense layers. It does not model word order. Use regularisation, dropout, class weights, validation early stopping and two fixed seeds. Vectorise strings on CPU before numerical GPU/TPU training.

Validation selects thresholds and the winner by recall under an illustrative 1% legitimate-message false-positive budget, then AP and fitting cost. This is an empirical budget, not a population guarantee. Do not refit on validation after choosing thresholds.

### Final evidence

Evaluate the untouched test once. Record accuracy, precision, recall, F1, AP, ROC-AUC, FPR, false alerts per 1,000 legitimate messages, confusion counts and runtime. Plot PR/ROC curves and the winner's confusion matrix. Retain the validation-selected winner. Report group-bootstrap intervals and aggregate errors by length/class.

### Saved Colab run review

The user-saved run in commit [538b8cc](https://github.com/chamarairesh1982/ml-cybersecurity/commit/538b8cc) contains successful execution outputs. These are historical observations from that runtime, not a locally repeated real-data experiment. The saved source omitted the validation-selection and final-test cells, with neural source carrying their old outputs. Those cells have been restored from the original notebook. Current outputs are cleared to avoid associating historical results with repaired source.

Validation selected the word+character linear SVM at threshold -0.074392: recall 99.13%, FPR 0.9494%, AP 0.998727. On the 2,531-row test partition it found 929 of 938 phishing-labelled emails and falsely flagged 14 of 1,593 safe-labelled emails (9 misses). Test precision was 98.52%, recall 99.04%, F1 98.78%, AP 0.998188 and FPR 0.8788%, or 8.79 false alerts per 1,000 safe-labelled emails. The group-bootstrap 95% FPR interval was approximately 0.4567%–1.3834%; the point meets the 1% budget but does not guarantee a population rate below 1%.

The six classical searches totalled approximately 43.0 minutes. The two word+character searches accounted for 30.9 minutes (72%). The two neural fits totalled approximately 49 seconds, excluding preprocessing and other stages. These times do not establish total notebook duration or separately measure feature extraction and solver time.

The repair caches fold-specific training transforms across classifier settings and compatible model families, and builds bootstrap group membership with stable sorting. Models, search grids, partitions and validation policy are preserved. Synthetic checks verify cached/uncached equivalence and bootstrap equivalence. A fresh Colab run is needed to measure real-data speedup; cached training matrices consume temporary runtime disk space. Classical searches still use CPU in an accelerator runtime.

Further model development after examining these test results needs a new independent holdout.

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
