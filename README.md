# ml-cybersecurity

Four independent learning experiments, each implemented entirely in a Google Colab Jupyter notebook. No standalone Python scripts, lectures, personal details, datasets or trained models are committed.

| Section | Open notebook | Current revision |
|---|---|---|
| 1 — phishing | [Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section1_phishing/section1_phishing.ipynb) | v2: grouped fitting, stopping, selection and policy |
| 2 — intrusion | [Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section2_intrusion/section2_intrusion.ipynb) | v3: independent neural stopping and precise score thresholds |
| 3 — anomaly | [Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section3_anomaly/section3_anomaly.ipynb) | v2: Normal-only scaling safeguard and development workflow |
| 4 — ransomware payments | [Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/section4_ransomware/section4_ransomware.ipynb) | v2: recent chronological fitting with all rare positives retained |

## Run

Open the latest GitHub notebook in a fresh Colab runtime and choose **Runtime → Run all**. Public data loads in Colab; no upload, Drive mount or credentials are needed. The first code/configuration cells control optional neural comparators and runtime cost. Classical models run on CPU; numerical TensorFlow models support GPU/TPU strategies. Small numerical tasks may not benefit from a TPU. Updated accelerator execution still requires verification in your Colab runtime.

Each notebook now defaults to `RUN_HISTORICAL_TEST=False`. The original test experiments have already been inspected, so default runs produce development evidence. Set the flag to True only for an explicitly historical replay. Repeated runs, additional seeds and newly partitioned rows from an inspected corpus do not establish independent improvement. A new compatible holdout is needed for final validation.

Aggregate reports remain inside Colab:

- Section 1: `/content/section1_results/v2_development`
- Section 2: `/content/section2_results/v3_development`
- Section 3: `/content/section3_results/v2_development`
- Section 4: `/content/section4_results/v2_development`

The notebooks do not publish results or models to GitHub. Record actual evidence before drawing conclusions; no model is claimed to be universally best.

## What changed after saved-run review

Section 1's historical text classifier performed well, but validation previously served several roles. The revised experiment separates grouped fitting, neural stopping, model selection and independent background-policy calibration. Classical TF-IDF caches remain fold-specific; stemming and structural models provide ablations.

Section 2's saved category winner was Extra Trees, with development macro-F1 about 0.757. The revised experiment reserves grouped neural stopping data for every candidate. Neural probability outputs now convert to float64 before attack-score subtraction, preventing nextafter thresholds from rounding onto tied scores. Policy group-count assertions check the declared rank.

Section 3's saved Isolation Forest had historical AP about 0.959, recall 57.5% and Normal false-alert rate 1.10%. Some attack types were almost entirely missed. A training-only floor on robust numerical scale prevents tiny interquantile ranges from dominating reconstruction models. Normal-only fitting remains label-assisted for model selection. Anomaly scores are not attack probabilities.

Section 4's previous model caught only 1 of 301 labelled ransomware addresses in historical testing despite 99.1% accuracy. Its random fitting cap retained only 257 of 3,465 positives. The revision keeps all training positives, samples background with explicit inclusion/class-balancing weights, and fits on data before July 2016. Separate stopping, selection and policy cohorts cover July–August, September–October and November–December 2016. Complete forward validation covers 2014, 2015 and early 2016. The sampled background labels are incomplete; this is historical payment screening after a daily graph window closes.

## Evidence and sources

[REPORT.md](REPORT.md) records the saved findings, changes and verification limits. [DATASET_SELECTION.md](DATASET_SELECTION.md) records public sources, licences, fingerprints and label limitations. [AGENTS.md](AGENTS.md) preserves the notebook-only structure and evaluation rules.

Local checks use synthetic fixtures only. Updated real-data performance has not been measured. Clear outputs in edited notebooks before publishing; preserve unrelated user-saved runs. Public GitHub account ownership remains visible.
