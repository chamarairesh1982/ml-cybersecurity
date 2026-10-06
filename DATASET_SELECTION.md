# Dataset selection before training

No dataset is selected, downloaded, or redistributed in this repository. Choose one section at a time and verify the provider's current documentation before use.

| Section | Required evidence | Reject or narrow the claim when |
|---|---|---|
| Phishing | Genuine phishing labels, legitimate controls, label methodology, text access, source/campaign grouping | Labels identify only spam; duplicates cross splits; identifiers reveal the answer |
| Intrusion | Flow features, documented attack classes, capture/session identifiers, independent holdout | Train/test share flows or collection artefacts dominate the labels |
| Anomaly | Normal traffic provenance, documented contamination, separate attack-labelled evaluation data | Training normality is unverified or attack labels drive an allegedly unsupervised threshold |
| Ransomware | Recorded ordered events, benign controls, process/sample IDs, family/environment metadata | Only static headers exist but the report claims behaviour or prevention |

Before choosing: verify the official provider, licence, download availability, class definitions, size, Colab memory needs, and privacy. Record a file checksum locally for reproducibility without committing the raw data. Prefer stronger provenance and independent evaluation over a high advertised accuracy.

Do not redistribute email bodies, network identifiers, proprietary logs, malware binaries, or data with unclear reuse rights. Keep exact data paths and any private audit material local. Dataset names and source links will be added after current provider documentation has been checked.
