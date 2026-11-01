# Entropy-Based Privacy Risk Analysis

A small, exploratory implementation of an entropy-based method for examining how quasi-identifiers can expose a sensitive attribute in tabular data. The notebooks use a reproducible, synthetic dataset; no real or personal data is included.

The analysis follows S.-H. Kim, C. Jung, and Y.-J. Lee, [“An entropy-based analytic model for the privacy-preserving in open data”](https://doi.org/10.1109/BigData.2016.7841035), *2016 IEEE International Conference on Big Data*, pp. 3676–3684.

> This is an independent implementation, not the authors' code and not affiliated with them. Scores are exploratory indicators, **not a privacy guarantee**. A low score does not establish that a dataset is safe to release.

This is specifically an exploratory example, not a production-ready privacy assessment.

## Repository Contents

| File | Purpose |
|---|---|
| `dataset_create_and_explore.ipynb` | Creates and explores a 1,000-row synthetic dataset, then writes `synthetic_dataset.csv`. |
| `entropy_privacypreserving.ipynb` | Examines matching probabilities, entropy, re-identification risk, and quasi-identifier sensitivity. |
| `entropy.py` | Provides `shannon_entropy(data)`, the empirical Shannon entropy in bits. |
| `test_entropy.py` | Unit tests for the entropy helper. |

The generated CSV is ignored by git. Run the dataset notebook before the analysis notebook.

The synthetic dataset contains `text_message` (the example sensitive attribute), `url`, `language`, `country`, `device`, and `star_review`.

## Quick Start

Use Python 3.10 or newer. From the repository directory:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
python -m pip install -r requirements.txt
jupyter notebook
```

Run `dataset_create_and_explore.ipynb` first, then `entropy_privacypreserving.ipynb`.

Run the unit tests with:

```bash
python -m pytest
```

## Method at a Glance

- The **L-entity** is the dataset being considered for release, including its sensitive attribute.
- The **I-entity** represents an attacker’s auxiliary information, modeled here as quasi-identifiers.
- For each quasi-identifier group, matching probabilities describe the distribution of sensitive values.
- Per I-entity, the notebooks calculate matching entropy $H$, maximum entropy $H_{max} = \log_2(n)$, and relative entropy $D = H_{max} - H$.
- The reported risk is $D / H_{max} \times 100$; dataset risk is the maximum entity risk. The sensitivity analysis removes one quasi-identifier at a time and compares the resulting risk.

These metrics depend on the data, attribute choices, and modeling assumptions. They should not be used alone to make release decisions.

## License and Citation

The project is available under the Apache License 2.0; see [LICENSE](LICENSE). Citation metadata is provided in [CITATION.cff](CITATION.cff).
