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

The saved run in [commit db896bd](https://github.com/chamarairesh1982/ml-cybersecurity/commit/db896bd) completed without saved errors. Validation selected the forest: validation macro-F1 0.748261, historical filtered-test macro-F1 0.550922 and accuracy 0.749803. At the alert threshold, historical attack recall was 0.749296 and row FPR 0.026799: 823 false alerts and 3,739 missed attacks. Analysis recall was zero. The historical test contained 45,624 deduplicated, non-overlapping flows; these are not original benchmark row-weighted metrics.

The 95% group-bootstrap intervals were macro-F1 [0.532296, 0.567848], alert recall [0.740876, 0.755662], and row alert FPR [0.024768, 0.028599]. Classical searches totalled 18.4 minutes; neural fits totalled 4.4 minutes, excluding other stages. The baseline outputs remain available in Git history. Current outputs are cleared so that they cannot be mistaken for version 2 results.

### Version 2 development protocol

Keep the pinned corpus, integrity checks, schema/label audit, invalid-value handling, conflicting/consistent duplicate exclusions, identity/target exclusions and approximate core-feature grouping. Audit cleaning retention by class and print category support for all development partitions. Reserve fixed grouped fitting, model-selection and alert-calibration partitions, approximately 60/20/20. All preprocessing and grouped CV remain inside fitting data. No lucky seed searches or synthetic oversampling outside folds.

Compare prior, logistic regression, regularised forest, randomized Extra Trees, L2-regularised histogram boosting and the core-feature ablation. Hyperparameters maximise mean grouped-CV macro-F1 minus fold standard deviation; this is a stability heuristic, not a confidence bound. Record train/CV gaps and macro recall. Bound worker and numerical-library threads to limit nested parallelism. The neural comparator uses normalized square-root inverse-frequency weights and a fixed-taxonomy macro-F1 callback for early stopping, with two declared seeds. Numerical CPU smoke execution verifies the changed callback; accelerator execution remains unverified.

Freeze the category classifier using model-selection macro-F1 before accessing policy predictors/scores. Calibrate each predeclared candidate on the separate policy partition. Take the maximum Normal-flow attack score per approximate related-feature group; select a conservative order-statistic rank with a binomial-tail criterion. This targets 1% Normal-group false-alert probability with 95% confidence only under independent, exchangeable group scores. It does not guarantee row FPR or deployment performance. Exclude score ties conservatively; if independent-group support is too small, report a reject-all policy. Policy attack labels measure recall afterward and never choose the threshold. Candidate bounds are individual, not simultaneous, and the model winner cannot change after calibration.

Print model-selection per-class metrics, policy recall, row/group FPR, threshold ranks and support. PSI covariate diagnostics use fitting-only numeric bins; they do not establish drift causality. Export versioned aggregate evidence and fingerprints of all three development partitions in Colab, without rows or models.

The published test is already inspected and therefore not an untouched holdout. Run all defaults to development-only evidence; optional replay is explicitly historical and excludes development overlaps as before. A new compatible independent capture with verified provenance and groups is still required for final validation. No new dataset was downloaded locally and no improved real-data scores are claimed.

### Verification and limits

Notebook/schema/syntax checks and synthetic end-to-end tests exercise cleaning, grouped splits, candidate training, selection, conservative policy ranks, ties, malformed scores, insufficient-group fallback, exports, disabled benchmark fetch, optional replay and its repeat guard. CPU neural checks cover both seeds, macro-F1 history and normalized weights. Synthetic scores are code checks, not benchmark performance.

Historical synthetic attacks, label-dependent exclusions, approximate group independence, lack of timestamps/session IDs and source shift limit practical conclusions. Conservative calibration may sacrifice substantial recall and cannot correct population shift on its own.

## Section 3 — Normal-only network anomaly detection

The standalone Colab notebook uses a pinned NSL-KDD archival mirror, with original provider/paper attribution and explicit historical-benchmark limitations. Its security question is whether deviations from a trusted Normal reference support attack triage. Anomaly scores are not attack probabilities. No real-data results are claimed yet.

Audit schema, labels, missing/invalid numerics and feature-identical binary-label conflicts. Deduplicate consistent features, record per-label retention and any duplicate groups with multiple attack names. For binary-consistent duplicates, the first representative supplies its attack name; attack-name analyses inherit that ambiguity. Difficulty and labels never enter predictors. Group four-significant-digit numeric features and categories before fixed development splits; these are feature proxies, not session/campaign ground truth.

Fit imputation, log transforms, robust scaling and infrequent-category encoding only on Normal fitting references. Append Normal-reference unseen-category flags and audit coverage. Normal-only stopping data, mixed labelled model-selection data and separate policy data have disjoint groups. Sample complete fitting groups deterministically up to 12,000 rows for all candidates, report exclusions, and acknowledge possible loss of legitimate Normal modes.

Tune PCA reconstruction at .80/.95 retained variance, MiniBatch K-means with 8/32 clusters and Isolation Forest at 256/1,024 subsamples in three training-only grouped folds. Each fold fits fresh Normal-only encoding and a capped Normal reference, then scores its mixed training-fold holdout. Mean AP minus fold standard deviation chooses a setting per family; this label-assisted stability heuristic is not a confidence bound. Normal stopping/selection/policy/test data are excluded from CV. Compare the chosen families with robust distance, a fixed Normal-rank ensemble and optional novelty-mode LOF. Silhouette measures Normal cluster geometry rather than attack correctness. Two optional autoencoders use Normal-only reconstruction targets, Huber loss, regularisation and Normal-only stopping; anomaly scoring uses declared MSE. Score directions increase with anomaly.

Choose the benchmark model on labelled selection AP, then fitting cost. This is label-assisted model selection, despite one-class fitting. Freeze the winner before calibrating each predeclared detector on policy Normal-group maximum scores. Conservative binomial order-statistic thresholds target group risk only under independent/exchangeable scores; too little support causes explicit reject-all. They do not guarantee row FPR or deployment safety.

Fetch the publisher test only after decisions freeze, claim it with a repeat guard, and exclude overlap with the entire cleaned development pool. Report the filtered population, class/attack support, AP/ROC-AUC, alert precision/recall/F1, confusion counts, row/group FPR, false-alert workload and fitting/inference cost. Preserve the frozen winner and compare reject-all. Report per-attack/protocol errors, name novelty relative to development labels and group-bootstrap intervals. Name novelty is not a zero-day claim. Export aggregate evidence and split/reference fingerprints in Colab without raw records or fitted models.

**Real-data outcomes: pending Colab execution.** Synthetic end-to-end checks cover schema/integrity failures, cleaning exclusions, disjoint groups, Normal-only encoding, all classical candidates including LOF, calibration ranks/ties/fallback, overlap filtering, one-test guard, metrics, bootstrap and strict JSON exports. Numerical CPU checks cover both autoencoder seeds and batched reconstruction scores; actual GPU/TPU execution remains unverified. No real dataset was downloaded locally.

## Section 4 — ransomware-linked payment screening

The standalone Colab notebook implements supervised ranking of newly observed Bitcoin addresses from UCI BitcoinHeist. This is historical payment screening after a daily graph window closes, not endpoint encryption detection. White is incompletely labelled background; sample prevalence is affected by daily background caps and graph filtering. No real-data performance is claimed.

Download the official archive only in Colab memory, record runtime SHA-256 and source/version metadata, validate ZIP/schema/calendars, then parse the opened period in chunks. No independent publisher digest was established, so source identity is recorded rather than presented as an authenticated immutable pin. Missing/nonfinite numerical cells are imputed only inside fitting boundaries; invalid targets/addresses/calendars, negative measurements and ambiguous address-day copies are excluded. Retain first-observation addresses and prevent dirty earlier observations from promoting recurring addresses into later cohorts. Print cleaning and exclusion counts without addresses.

Use fitting data through 2015, separate early-2016 neural stopping, late-2016 model selection, early-2017 policy calibration and July-2017–2018 final test. Two expanding-window training CV folds validate on 2014/2015. Uniform label-blind caps bound fitting/CV cost while all later evaluation partitions remain uncapped. Identity, calendar and family fields never enter predictors. Median imputation, log1p and standardisation fit independently inside each training fold. Three fixed ratios have a core-feature boosting ablation.

Compare prior, weighted logistic regression, regularised forest, regularised histogram boosting, the core-feature ablation, a fixed forest/boosting ensemble and two optional weighted numerical neural seeds with dropout/L2. Forward-fold mean AP minus fold standard deviation selects each classical configuration; this is a heuristic. Neural stopping uses its distinct temporal partition. Selection AP chooses the final model, with fitting cost breaking exact ties. Freeze before calibrating a tie-conservative threshold targeting at most 1% observed background alerts on the separate policy partition. This is an empirical sample budget, not a population confidence bound or deployment guarantee. Never refit after calibration.

Guard final test evaluation once, exclude all earlier observed addresses and preserve the frozen model/threshold. Report AP/ROC-AUC, accuracy/F1, precision/recall, confusion counts, background-alert rate/workload, cost, PR/confusion plots, family/time/name-novelty errors and fitting-quantile drift. Calendar-week block bootstrap intervals for operating metrics acknowledge residual graph/time dependence; ranking metrics are point estimates. Optional classical permutation importance uses selection data, not test-driven retuning. Export aggregate evidence and partition fingerprints only, without addresses/rows/models.

**Real-data outcomes: pending Colab execution.** Synthetic checks cover calendar/leap-year handling, missing/invalid/duplicate/conflicting records, dirty first observations, recurring-address exclusion, chronological folds, training-only preprocessing, all five classical families, threshold ties/empty input, metrics, weekly bootstrap and drift. A full synthetic notebook run also passes model/ensemble selection, policy calibration, final-test evaluation/repeat guarding and strict aggregate-only exports with partition digests. Numerical CPU checks pass for both neural seeds and CPU strategy discovery. Degenerate bootstrap intervals are flagged and cannot bound unseen errors. Actual Colab GPU/TPU execution remains unverified. Existing user-saved Section 1/2 notebooks are preserved; Section 1 has pre-existing nonstandard saved-output metadata while its source validates after stripping outputs in memory.
