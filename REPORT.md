# ml-cybersecurity

Independent machine learning experiments for cybersecurity, one scenario at a time. Dataset and model choices follow the problem and evidence. No personal details, school identifiers, lecture files, datasets, or measured results are included.

## How we work

Define the security decision; assess suitable data; audit labels and duplicates; design independent training, validation, and test partitions; establish a simple baseline; compare justified candidates; evaluate held-out performance and explain failures.

There is no fixed dataset or algorithm checklist. Choose additional complexity only when the data and measured benefit justify its cost. Fit learned preprocessing on training data only. Use validation data for configuration and threshold selection. Evaluate the final test once.

## Scenario 1: experiment design

The unit of prediction is one email using information available when it arrives. Confirm that labels represent phishing rather than only spam. Define the analyst review budget before selecting a threshold.

Before choosing data, assess provenance, collection period, label method, legitimate controls, licence, campaign/source grouping, privacy, and Colab memory needs. No dataset is selected yet.

Prefer independent time, campaign, or source holdouts. Inspect baseline errors before choosing candidate models. Report average precision, operating-point precision and recall, false-positive rate, confusion counts, false alerts per 1,000 legitimate messages, runtime, uncertainty, and performance under shift.

Current stage: problem definition and evaluation design. Dataset selection, model selection, training implementation, and measured conclusions are pending. Review the evidence from this scenario before moving on.

## Scenario 2: Network attack detection

Recognise suspicious network flows and distinguish attack categories when the available labels support that task.

Planned: begins after the previous scenario is reviewed. Data and models remain undecided.

## Scenario 3: Unusual activity detection

Prioritise departures from normal behaviour when attack labels are incomplete.

Planned: begins after the previous scenario is reviewed. Data and models remain undecided.

## Scenario 4: Ransomware behaviour screening

Flag suspicious recorded process activity early and assess unfamiliar families or collection environments.

Planned: begins after the previous scenario is reviewed. Data and models remain undecided.

## Evidence journal

Record provenance, licence, label limitations, audit exclusions, split independence, feature availability, model rationale, validation decisions, held-out metrics, figures, runtime, uncertainty, and errors. Conclusions must follow actual measurements.
