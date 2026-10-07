# Project instructions

This is an independent learning project. Keep personal details, student numbers, school names, course identifiers and submission framing out of project content.

## Structure

- Use four scenario folders, each with one self-contained Google Colab Jupyter notebook.
- Implement only the currently active scenario. Section 2 is active; Section 1 is implemented and Sections 3–4 remain placeholders until the user moves on.
- Put all runnable Python inside notebook code cells. Do not create, commit or depend on standalone .py files or notebook generators.
- Edit notebooks directly and preserve nbformat validity, stable cell IDs, a Python 3 kernelspec and clear teaching markdown.
- Never commit lectures, teaching scripts, datasets, raw messages, credentials, trained models or executed notebook outputs.
- Lectures and LearnPython materials in the parent workspace are read-only conceptual guidance. Do not copy identifying content.

## ML workflow

- Teach the relevant lecture concepts: foundations, profiling/EDA, cleaning, feature engineering, supervised models, neural learning, ensembles, evaluation and NLP. Reserve unsupervised modelling mainly for the anomaly scenario.
- Select public data based on the task, provenance, label quality, licence and evaluation feasibility. Verify official sources before changing dataset choice.
- Load public data directly in the Colab runtime using a pinned version and integrity check when available. Do not download datasets to the local machine.
- Never invent benchmark results or claim a universally best model. Select using declared validation criteria and report limitations.
- Audit schema, missing/empty data, duplicate/conflicting labels and class imbalance. Keep audit counts.
- Group related samples before splitting. Fit vectorisers, scaling, vocabulary, feature selection and resampling only inside training boundaries or CV folds.
- Use the same partitions for all candidates. Tune within training CV; use validation for thresholds/model decisions; evaluate the untouched test once.
- Compare simple baselines against justified classical, ensemble and neural candidates. More complex models must justify their cost.
- Explain why preprocessing fits the data; test aggressive text cleaning as an ablation.
- Report imbalance-aware ranking metrics, operating-point precision/recall, FPR/alert workload, confusion counts, uncertainty, runtime and errors.
- Use numerical TensorFlow inputs under GPU/TPU strategies. Perform string vectorisation on CPU; do not imply classical scikit-learn runs on TPU.
- Do not claim accelerator execution or real-data performance without running it. Clearly distinguish synthetic checks, CPU neural checks and actual Colab accelerator checks.

## Verification and publishing

- Validate all four notebooks, syntax (including IPython cells), output clearing, and exact repository file inventory.
- Test meaningful local logic with in-memory synthetic fixtures; do not fetch the real dataset locally.
- Keep test helpers out of repository .py files. No extra agent delegation is required.
- Review staged files for personal data, lectures, datasets and unexpected files before pushing.
- Use the existing repository remote and generic project Git identity; update README Colab links when paths change.
- Do not rewrite history or force-push for routine cleanup. Historical scaffolding may remain in earlier commits; keep the current tree clean.
