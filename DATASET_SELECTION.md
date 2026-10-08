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

This corpus supports practising the complete workflow; it is not claimed to be universally the best dataset.

## Section 2 public data

Use the [original UNSW-NB15 description and research-use terms](https://research.unsw.edu.au/projects/unsw-nb15-dataset), with a [pinned parquet mirror](https://huggingface.co/datasets/lacg030175/UNSW-NB15/blob/34ee5744ecb143db1b12623670f754f56c36b94b/README.md) for direct Colab loading.

- Revision: `34ee5744ecb143db1b12623670f754f56c36b94b`.
- Configuration: `standard`; avoid the mirror's differently constructed random configuration.
- Training artifact: `standard/train-00000-of-00001.parquet` (12,773,520 bytes); SHA-256 `0c4a4884abfe24d4545c5ed8cbe1146525cc4ac5c8e0dc8c2b654309a32616ed`.
- Test artifact: `standard/test-00000-of-00001.parquet` (6,280,567 bytes); SHA-256 `70292cae81a8f24aa89ed6c74b01686db36b0750ef9af94da7cdc54e166be598`.
- Provider metadata reports 175,341 training and 82,332 test rows before notebook cleaning. Schema contains flow measurements, protocol/service/state, attack category and binary label; targets and identity fields never enter predictors.
- Original terms grant academic research use and request attribution, while commercial use requires author agreement. The mirror's broader CC-BY claim is not assumed to override those terms. No dataset is redistributed here.
- The mirror claims temporal separation, but reliable timestamps/session IDs are absent from the selected artifact. We describe a publisher benchmark split, not independently verified chronological evaluation.
- Historical replay metrics use deduplicated test rows whose rounded core-feature groups are absent from all development data. Report counts and acknowledge this different evaluation population.
- The published test was inspected in the saved Section 2 run. Version 2 disables its replay by default and labels any replay non-independent. No new compatible external holdout has been selected or verified; revised model performance is still unmeasured on independent data.

All real-data fetching occurs in Colab runtime memory. Local checks use synthetic in-memory fixtures only. Sections 3–4 remain undecided.
