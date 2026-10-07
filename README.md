# ml-cybersecurity

Independent learning experiments in four self-contained Google Colab notebooks. Sections 1 and 2 are implemented; Sections 3–4 reserve future work. Section 2 is the current scenario.

| Folder | Notebook | Status |
|---|---|---|
| section1_phishing | [Open Section 1 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section1_phishing/section1_phishing.ipynb) | Saved run reviewed; repaired source and feature caching |
| section2_intrusion | [Open Section 2 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section2_intrusion/section2_intrusion.ipynb) | Full experiment; run for results |
| section3_anomaly | section3_anomaly.ipynb | Placeholder |
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

Open its Colab link and run cells in order. The notebook fetches pinned UNSW-NB15 training parquet into Colab memory, reserves grouped validation data, and compares a prior baseline, logistic regression, random forest, histogram gradient boosting, a core-feature ablation and two neural seeds. The published test partition is fetched only after validation choices freeze. Duplicate and core-feature-group overlaps are excluded and counted; results describe that novelty subset rather than the unmodified published benchmark.

Review macro/per-class metrics, multiclass confusion and PR curves, the separate attack-alert threshold, false-alert workload, group-bootstrap intervals and protocol error slices. Aggregate evidence stays in `/content/section2_results`. No local dataset download or upload is needed. The first cell installs download/parquet extras. Major classical models use CPU; the numerical neural model supports TensorFlow GPU/TPU strategies, pending actual accelerator verification.

All runnable Python lives in notebook cells. No standalone .py file or generator is required. The first cell installs small extras; Colab provides major scientific libraries. Do not indiscriminately upgrade TensorFlow on a managed accelerator runtime. Clear outputs before committing.

## Learning process

The experiment applies lecture concepts: foundations, preparation/EDA, feature engineering, supervised learning, neural networks, ensemble comparison, evaluation and NLP. Unsupervised modelling is reserved mainly for Section 3.

Compare prior, word/character TF-IDF linear models, a text-cleaning ablation, structural models, a random forest and an embedding-based neural model. Select on validation recall under a declared false-positive budget and evaluate the untouched test once. Complexity must earn its cost.

Use the [public Phishing Email Dataset mirror](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset), attributed to the [original provider](https://www.kaggle.com/datasets/subhajournal/phishingemails). See DATASET_SELECTION.md for provenance and limitations. Section 1 historical scores are attributed to the saved Colab run in REPORT.md; notebook outputs remain cleared. Accelerator execution of updated code must be verified in the actual Colab runtime.

AGENTS.md preserves the notebook-only structure. REPORT.md is an evidence journal. Project files omit personal and school identifiers. Public account ownership remains visible. Lectures, teaching scripts, datasets, credentials, models and raw message outputs are excluded.
