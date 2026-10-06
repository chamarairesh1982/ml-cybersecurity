# ml-cybersecurity

Independent learning experiments in four self-contained Google Colab notebooks. Work one scenario at a time: Section 1 is implemented; Sections 2–4 reserve future work.

| Folder | Notebook | Status |
|---|---|---|
| section1_phishing | [Open Section 1 in Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section1_phishing/section1_phishing.ipynb) | Full experiment; run for results |
| section2_intrusion | section2_intrusion.ipynb | Placeholder |
| section3_anomaly | section3_anomaly.ipynb | Placeholder |
| section4_ransomware | section4_ransomware.ipynb | Placeholder |

## Run Section 1

1. Open the Colab link above.
2. Choose a CPU, GPU or TPU runtime. Classical models use CPU; the numerical TensorFlow comparator supports accelerator strategies.
3. Run cells in order, or use **Runtime → Run all** for the declared full experiment.
4. Colab fetches the pinned public CSV into runtime memory and verifies SHA-256. No local dataset download, manual upload, Drive mount or credential is needed.
5. Review audit/cleaning counts, duplicate grouping, training EDA, grouped CV, neural curves, validation selection, final test, uncertainty and aggregate errors.
6. Aggregate evidence is written to `/content/section1_results` in Colab. Nothing is published to GitHub by the notebook.

All runnable Python lives in notebook cells. No standalone .py file or generator is required. The first cell installs small extras; Colab provides major scientific libraries. Do not indiscriminately upgrade TensorFlow on a managed accelerator runtime. Clear outputs before committing.

## Learning process

The experiment applies lecture concepts: foundations, preparation/EDA, feature engineering, supervised learning, neural networks, ensemble comparison, evaluation and NLP. Unsupervised modelling is reserved mainly for Section 3.

Compare prior, word/character TF-IDF linear models, a text-cleaning ablation, structural models, a random forest and an embedding-based neural model. Select on validation recall under a declared false-positive budget and evaluate the untouched test once. Complexity must earn its cost.

Use the [public Phishing Email Dataset mirror](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset), attributed to the [original provider](https://www.kaggle.com/datasets/subhajournal/phishingemails). See DATASET_SELECTION.md for provenance and limitations. No real-data scores are pre-filled or claimed. GPU/TPU execution must be verified in the actual Colab runtime.

AGENTS.md preserves the notebook-only structure. REPORT.md is an evidence journal. Project files omit personal and school identifiers. Public account ownership remains visible. Lectures, teaching scripts, datasets, credentials, models and raw message outputs are excluded.
