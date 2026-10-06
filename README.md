# COMP70049-Assignment_2026

[Open in Google Colab](https://colab.research.google.com/github/chamarairesh1982/COMP70049-Assignment_2026/blob/main/COMP70049-Assignment_2026.ipynb)

Independent learning project about machine learning for cybersecurity. No personal details, lecture materials, datasets, or measured results are included.

## Start here

Open `COMP70049-Assignment_2026.ipynb` in Google Colab using **File → Upload notebook**, or use Colab's GitHub tab after this repository is published. The notebook is compatible with Python 3.

Work through the sections in order:

1. Email phishing detection: executable classical and optional LSTM workflow; bring an authorised labelled CSV.
2. Network intrusion classification: experiment design, implementation pending.
3. Anomaly detection: experiment design, implementation pending.
4. Ransomware behaviour screening: experiment design, implementation pending.

Read `REPORT.md` for the report companion and `DATASET_SELECTION.md` before choosing data. No dataset is automatically downloaded. In Colab, upload your own CSV through the Files sidebar, set `DATA_PATH`, and run Section 1 in order. The CSV must contain `text` and numeric `label` (0 legitimate, 1 phishing); optional `group` identifiers keep related messages together. The workflow stops clearly if data are missing or invalid. Enable `RUN_LSTM` to train the optional deep learning comparator.

For local use: install `requirements.txt`, then open the notebook in Jupyter. TensorFlow is optional for the classical workflow. Plot and metric outputs appear only after training; no results are pre-populated. Do not commit executed notebook outputs or data.

`build_notebook.py` regenerates the notebook and overwrites notebook edits, so edit the generator when maintaining its content.

## Privacy

The learning files omit names, contact information, and student identifiers. GitHub account ownership remains visible on a public repository. Use a generic Git author and GitHub's private/noreply email if committing locally. Inspect all files and clear notebook outputs before publishing changes.
