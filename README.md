# entropy-measure-privacy

Entropy-based privacy risk analysis for a tabular dataset, following the method in:

S.-H. Kim, C. Jung, and Y.-J. Lee, "An entropy-based analytic model for the privacy-preserving in open data,"
2016 IEEE International Conference on Big Data (Big Data), Dec. 2016, pp. 3676–3684.
doi: [10.1109/BigData.2016.7841035](https://doi.org/10.1109/BigData.2016.7841035)

The goal is to get an overall sense of how privacy-sensitive a dataset is, and which quasi-identifiers
make it sensitive. The data used here is synthetic.

> **Note:** This is an independent implementation based on the paper above. It is not the authors' code and is not
> affiliated with them. The results are exploratory and are **not a privacy guarantee**: a low risk score does not
> mean a dataset is safe to release.

## Notebooks

| Notebook | Purpose |
|---|---|
| `dataset_create_and_explore.ipynb` | Generates a 1000-row synthetic dataset, describes it, and writes `synthetic_dataset.csv` |
| `entropy_privacypreserving.ipynb` | Computes matching probabilities, entropy measures, re-identification risk, and per-column sensitivity |

Run `dataset_create_and_explore.ipynb` first: `synthetic_dataset.csv` is git-ignored and must be generated locally.

### Dataset columns

| Column | Description |
|---|---|
| `text_message` | Short example text messages (sensitive attribute) |
| `url` | Example URLs |
| `language` | Language of the message |
| `country` | Country of origin |
| `device` | Device type (Mobile / Desktop / Tablet) |
| `star_review` | 5-star review rating (1–5) |

## Code

| File | Purpose |
|---|---|
| `entropy.py` | `shannon_entropy(data)`: Shannon entropy, in bits, of the empirical distribution of a sequence |
| `test_entropy.py` | pytest tests for `entropy.py` |

## Method summary

- **L-entity**: the dataset to be released, including the sensitive attribute.
- **I-entity**: what an attacker knows, i.e. the quasi-identifiers only.
- **Matching probability** P(s|i): share of each sensitive value among records with the same quasi-identifiers.
- **Matching entropy** H, **maximum entropy** H_max = log2(n), and **relative entropy** D = H_max − H per I-entity.
- **Risk** = D / H_max × 100; dataset risk is the maximum entity risk.
- **Sensitivity analysis**: drop one quasi-identifier at a time to see which contributes most to risk.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
pip install -r requirements.txt
jupyter notebook
```

Then run `dataset_create_and_explore.ipynb`, followed by `entropy_privacypreserving.ipynb`.

Run the tests with:

```bash
pytest
```

## Dependencies

See [requirements.txt](requirements.txt): pandas, numpy, matplotlib, scipy, Jupyter, and pytest.

## License

Apache License 2.0. See [LICENSE](LICENSE).
