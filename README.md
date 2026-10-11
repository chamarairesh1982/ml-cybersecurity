# ml-cybersecurity

Independent learning experiments in four self-contained Google Colab notebooks. Sections 1–3 are implemented; Section 4 reserves future work. Section 3 is the current scenario.

| Folder | Notebook | Status |
|---|---|---|
| section1_phishing | [Open Section 1 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section1_phishing/section1_phishing.ipynb) | Saved run reviewed; repaired source and feature caching |
| section2_intrusion | [Open Section 2 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section2_intrusion/section2_intrusion.ipynb) | Version 2 development workflow; historical replay optional |
| section3_anomaly | [Open Section 3 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section3_anomaly/section3_anomaly.ipynb) | Normal-only anomaly learning; real-data run pending |
| section4_ransomware | section4_ransomware.ipynb | Placeholder |

## Run Section 1

1. Open the Colab link above.
2. Choose a CPU, GPU or TPU runtime. Classical models use CPU; the numerical TensorFlow comparator supports accelerator strategies.
3. Run cells in order, or use **Runtime → Run all** for the declared full experiment.
4. Colab fetches the pinned public CSV into runtime memory and verifies SHA-256. No local dataset download, manual upload, Drive mount or credential is needed.
5. Review audit/cleaning counts, duplicate grouping, training EDA, grouped CV, neural curves, validation selection, final test, uncertainty and aggregate errors.
6. Aggregate evidence is written to `/content/section1_results` in Colab. Nothing is published to GitHub by the notebook.

The saved run and runtime findings are recorded in REPORT.md. The latest notebook restores missing validation/test cells and caches training feature extraction in `/content/section1_feature_cache`. Open the latest GitHub version in a fresh Colab runtime rather than using an older open copy. Caching consumes temporary disk space; set `CACHE_FEATURES=False` to disable it. A fresh run is needed to measure speedup.

## Run Section 2

Open the latest Colab link in a fresh runtime and run cells in order. Version 2 fetches the same pinned UNSW-NB15 training parquet only in Colab. Fixed, disjoint related-feature groups divide fitting data, model-selection data and alert-policy calibration data. Compare prior, logistic regression, regularised forest, Extra Trees, regularised histogram boosting, a core-feature ablation and two neural seeds. Grouped CV uses a declared stability heuristic; neural early stopping follows macro-F1. CPU worker threads are bounded to reduce nested parallelism.

Review class support, train/CV gaps, model-selection per-class metrics and policy calibration. Freeze the category winner before calibrating alerts. The conservative threshold targets Normal-group false-alert risk under independent, exchangeable group assumptions; it cannot guarantee deployment or row-level FPR. Too few calibration groups produce an explicitly labelled reject-all policy. Covariate diagnostics use fitting-only quantile bins. Aggregate evidence stays in `/content/section2_results/v2_development`.

The published test set has already been inspected. `RUN_HISTORICAL_TEST=False` is the default, so Run all completes development evidence without fetching it. Optional replay reports historical metrics, confusion/PR curves, group-bootstrap intervals and errors on a deduplicated novelty subset. It is not a new independent test or proof of improvement. Independent final validation requires a genuinely new compatible capture. No local dataset download or upload is needed. Major classical models use CPU; the numerical neural model supports TensorFlow GPU/TPU strategies, pending verification of this version in Colab.

## Run Section 3

Open the Colab link in a fresh runtime and run cells in order. The notebook fetches pinned NSL-KDD training data into Colab memory, audits labels/numeric values/duplicates, and forms disjoint rounded-feature groups. Normal-only reference fitting and stopping data remain separate from mixed model-selection and policy-calibration data. All imputation, log scaling, robust scaling and encoding fit only on the declared capped Normal reference.

Tune PCA variance retention, K-means cluster count and Isolation Forest subsampling in three grouped training-only folds, fitting fresh Normal-only encoding/detectors in each fold. Compare the chosen classical families with robust distance, a fixed Normal-rank ensemble and two optional autoencoder seeds on the separate selection partition. LOF is optional and disabled by default because scoring can be expensive. Classical methods use CPU; numerical autoencoder strategies support GPU/TPU, pending actual Colab verification. The common Normal reference cap is 12,000 rows sampled as complete groups within each fitting boundary, with exclusions reported.

Labels choose the benchmark winner by selection AP, so the whole experiment is label-assisted despite Normal-only detector fitting. Freeze the model, calibrate a conservative Normal-group alert threshold on a separate partition, then fetch/evaluate the publisher test once. Related-feature overlap filtering changes the evaluation population. Review false alerts, missed attacks, per-attack/name-novelty errors, group-bootstrap intervals and timing; no modern deployment or zero-day claim is implied. Aggregate evidence stays in `/content/section3_results`. Source identity uses a pinned mirror commit, Git blob/byte checks and a recorded runtime SHA-256; no real dataset is downloaded locally.

All runnable Python lives in notebook cells. No standalone .py file or generator is required. The first cell installs small extras; Colab provides major scientific libraries. Do not indiscriminately upgrade TensorFlow on a managed accelerator runtime. Clear outputs in edited notebooks before committing; preserve unrelated user-saved runs.

## Learning process

The experiments apply lecture concepts: foundations, preparation/EDA, feature engineering, supervised learning, neural networks, ensemble comparison, evaluation and NLP. Section 3 adds clustering, dimensionality reduction and novelty detection.

Compare prior, word/character TF-IDF linear models, a text-cleaning ablation, structural models, a random forest and an embedding-based neural model. Select on validation recall under a declared false-positive budget and evaluate the untouched test once. Complexity must earn its cost.

Use the [public Phishing Email Dataset mirror](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset), attributed to the [original provider](https://www.kaggle.com/datasets/subhajournal/phishingemails). See DATASET_SELECTION.md for provenance and limitations. Section 1 historical scores are attributed to the saved Colab run in REPORT.md; notebook outputs remain cleared. Accelerator execution of updated code must be verified in the actual Colab runtime.

AGENTS.md preserves the notebook-only structure. REPORT.md is an evidence journal. Project files omit personal and school identifiers. Public account ownership remains visible. Lectures, teaching scripts, datasets, credentials, models and raw message outputs are excluded.
