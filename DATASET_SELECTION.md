# Section 1 public data

Selected for an accessible reproducible text-classification learning experiment: [zefang-liu/phishing-email-dataset](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset).

- Original source attributed by the mirror: [Phishing Email Detection on Kaggle](https://www.kaggle.com/datasets/subhajournal/phishingemails).
- Mirror card lists LGPL-3.0. Preserve attribution and check original rights before redistribution. This repository distributes no dataset.
- Pinned revision: `34085a032c123ca237f314a01a67909cdea35e34`.
- File: `Phishing_Email.csv`, approximately 52 MB.
- Provider-reported SHA-256: `18ef4fff1acb8986f0ab01e83ede6025420c829656af5a377560fce17e153b97`.
- Expected fields: `Email Text`, `Email Type`; labels: `Safe Email`, `Phishing Email`.
- The notebook verifies identity, schema and labels, then measures actual counts at runtime.
- Fetching occurs in Colab memory, never the local workspace or Git.

## Interpretation limits

Provider labels are not independently verified. Reliable campaign IDs, timestamps and external source holdouts are not established by the mirror. Approximate content grouping reduces discovered template leakage but cannot prove campaign independence. Label noise and source artefacts may inflate metrics. This is a corpus-labelled benchmark; operational conclusions require independent current data.

This corpus supports practising the complete workflow; it is not claimed to be universally the best dataset. Data for other sections remain undecided.
