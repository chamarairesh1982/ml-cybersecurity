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

## Section 3 public data

Use [NSL-KDD's original provider description and citation terms](https://www.unb.ca/cic/datasets/nsl.html), attributed to M. Tavallaee, E. Bagheri, W. Lu and A. Ghorbani, *A Detailed Analysis of the KDD CUP 99 Data Set*, CISDA 2009. The provider permits use/redistribution with attribution but no longer supplies downloads. A [third-party archive](https://github.com/jmnwong/NSL-KDD-Dataset/tree/9d544d0eb9b87d7e2f43ff65733bdb644631d12f) reports restoration from the original site through the Wayback Machine.

- Pinned mirror commit: `9d544d0eb9b87d7e2f43ff65733bdb644631d12f`.
- `KDDTrain+.txt`: Git blob `20002897492adc110190a10509aa694f26f7f308`, 19,109,424 bytes.
- `KDDTest+.txt`: Git blob `b30e89605285a5ccd8cf8fd38dba72906c20d3dd`, 3,441,513 bytes.
- Commit, blob identities and sizes were verified through GitHub metadata without fetching actual data locally. Colab verifies the exact blob/byte identity and records SHA-256. Git SHA-1 identity does not establish adversarial collision resistance or independently prove provider authenticity.
- Expect 41 predictors, attack name and difficulty. Exclude both metadata/target fields from modelling. Normal eligibility uses provider labels; labelled development AP chooses the benchmark model. This is Normal-only fitting with label-assisted selection.
- Deterministic duplicate/contradiction filtering, rounded-feature groups and complete-group reference sampling change the population. Test overlap filtering uses all cleaned development-pool rows, not only selected Normal fitting rows.
- Historical selected attacks, offline host/content counters, absent reliable timestamps/session IDs, imperfect Normal coverage and approximate group independence limit modern operational inference. Attack-name novelty is not verified zero-day detection.

All real-data fetching occurs in Colab runtime memory. Local checks use synthetic in-memory fixtures only.

## Section 4 public data

Use [UCI BitcoinHeist Ransomware Address](https://archive.ics.uci.edu/dataset/526/bitcoinheistransomwareaddressdataset), [DOI 10.24432/C5BG8V](https://doi.org/10.24432/C5BG8V), licensed CC BY 4.0. Attribute the [original BitcoinHeist research](https://arxiv.org/abs/1906.07852). This repository redistributes no dataset.

- Official runtime source: `https://archive.ics.uci.edu/static/public/526/bitcoinheistransomwareaddressdataset.zip`; archive member `BitcoinHeistData.csv`. The download endpoint was checked with HEAD only, without downloading data locally.
- Provider reports 2,916,697 observations, approximately 225 MB CSV / 111 MB archive, spanning daily graph windows in 2009–2018.
- Measurements: length, weight, count, looped, neighbors and income in satoshis. Address/year/day and ransomware-family label are metadata, never predictors. Three fixed row-local ratios are compared against a core-feature ablation.
- No independently verified publisher digest was found. The notebook records runtime archive SHA-256, verifies ZIP CRC through reads, enforces a size envelope and validates schema. The URL is fixed but not an immutable content version. Optional externally verified SHA-256 can enforce a repeated artifact.
- White means not known to be ransomware, not verified benign. Background sampling was capped at 1,000 addresses per day; edges below 0.3 BTC were filtered. Precision and background-alert metrics cannot establish live-population accuracy.
- Retrospective labels have unknown historical availability. Earliest eligible address observations, discarded ambiguous/invalid first observations and exclusions of any previously observed address change the population. Address disjointness does not establish actor/campaign independence.
- Fixed chronological development and test boundaries prevent random time mixing. One archive includes the test period, but test rows are not retained/profiled until model and policy are frozen. Weekly block intervals still rely on approximate block independence and representativeness.

The experiment screens historical payment addresses after each daily feature window closes; it does not detect or prevent endpoint ransomware encryption. Real-data metrics and accelerator behaviour require a fresh Colab run. After test inspection, further tuning needs a new independent holdout.
