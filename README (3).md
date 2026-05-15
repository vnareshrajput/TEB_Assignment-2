# Law of Large Numbers — Snakemake Demo

## Output

![LLN plot for n=2000](plots/lln_for_n_2000.png)

---

## What This Does

Samples integers uniformly from `[1, n]` with increasing sample sizes `k`, then
box-plots the resulting sample means. As `k` grows the distribution tightens
around the theoretical expected value `(n + 1) / 2`, illustrating the Law of
Large Numbers.

---

## Quick Start

### Prerequisites

- Python 3.8+
- Snakemake
- matplotlib (`pip install matplotlib`)

### Run

```bash
# Clear previous outputs if they share the target filename
rm -f plots/lln_for_n_2000.png data/results.csv

snakemake --cores 1
```

The pipeline runs two rules:

| Rule | Script | Output |
|------|--------|--------|
| `simulate` | `scripts/simulate.py` | `data/results.csv` |
| `plot` | `scripts/plot.py` | `plots/lln_for_n_{n}.png` |

---

## Configuration (`config.yaml`)

```yaml
n: 2000          # integers drawn from [1, n]

k_values:
  - 5
  - 10
  - 25
  - 50
  - 100
  - 200
  - 1000
  - 2000

repeats: 10      # independent trials per k
```

Edit `config.yaml` and re-run `snakemake --cores 1` to test different settings.
