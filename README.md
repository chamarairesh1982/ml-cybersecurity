# ml-cybersecurity

Independent machine learning experiments for cybersecurity, one scenario at a time. Dataset and model choices follow the problem and evidence. No personal details, school identifiers, lecture files, datasets, or measured results are included.

[Open in Google Colab](https://colab.research.google.com/github/chamarairesh1982/ml-cybersecurity/blob/main/ml-cybersecurity.ipynb)

## How we work

Define the security decision; assess suitable data; audit labels and duplicates; design independent training, validation, and test partitions; establish a simple baseline; compare justified candidates; evaluate held-out performance and explain failures.

There is no fixed dataset or algorithm checklist. Choose additional complexity only when the data and measured benefit justify its cost. Fit learned preprocessing on training data only. Use validation data for configuration and threshold selection. Evaluate the final test once.

## Scenario order

1. Phishing email triage — current
2. Network attack detection — planned
3. Unusual activity detection — planned
4. Ransomware behaviour screening — planned

The notebook contains the roadmap and Scenario 1 design. We will add training code after selecting suitable data. REPORT.md is the experiment journal. build_notebook.py regenerates the output-free notebook.

Project files contain no student number or contact details. Public GitHub account ownership remains visible. Commits use a generic project identity. Keep data and executed outputs local.
