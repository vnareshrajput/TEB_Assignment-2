import argparse
import csv
from collections import defaultdict

import matplotlib.pyplot as plt


def parse_args():
    parser = argparse.ArgumentParser(
        description="Box-plot sample means to visualise the Law of Large Numbers."
    )
    parser.add_argument("--input",  required=True,       help="CSV file produced by simulate.py")
    parser.add_argument("--output", required=True,       help="Output image path (.png)")
    parser.add_argument("--n",      type=int, required=True, help="Upper bound used during simulation")
    return parser.parse_args()


def load_csv(filepath):
    """Read the CSV and group mean values by their sample size k."""
    grouped = defaultdict(list)
    with open(filepath, newline="") as fh:
        for row in csv.DictReader(fh):
            grouped[int(row["k"])].append(float(row["mean"]))
    return grouped


def build_plot(grouped, n, output_path):
    k_order = sorted(grouped.keys())
    data   = [grouped[k] for k in k_order]
    labels = [f"k={k}" for k in k_order]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.boxplot(data, tick_labels=labels)

    # Theoretical expected mean for Uniform[1, n]
    ax.axhline(y=(n + 1) / 2, linestyle="--")

    ax.set_xlabel("k values")
    ax.set_ylabel("Sample Mean")
    ax.set_title(f"Testing Draws for {n}")

    fig.savefig(output_path)
    print(f"Plot saved → {output_path}")


def main():
    args = parse_args()
    grouped = load_csv(args.input)
    build_plot(grouped, args.n, args.output)


if __name__ == "__main__":
    main()
