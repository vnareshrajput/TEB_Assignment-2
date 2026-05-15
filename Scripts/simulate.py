import argparse
import csv
import random


def parse_args():
    parser = argparse.ArgumentParser(
        description="Simulate sample means for the Law of Large Numbers demo."
    )
    parser.add_argument("--n",        type=int,           required=True, help="Upper bound of the integer range [1, n]")
    parser.add_argument("--repeats",  type=int,           required=True, help="Number of repetitions per k value")
    parser.add_argument("--k_values", type=int, nargs="+", required=True, help="List of sample sizes to test")
    parser.add_argument("--output",                       required=True, help="Destination CSV file path")
    return parser.parse_args()


def sample_means(n, k_values, repeats):
    """Return a list of {k, mean} dicts for every (k, repeat) combination."""
    records = []
    for k in k_values:
        for _ in range(repeats):
            draws = [random.randint(1, n) for _ in range(k)]
            records.append({"k": k, "mean": sum(draws) / k})
    return records


def write_csv(records, filepath):
    with open(filepath, "w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["k", "mean"])
        writer.writeheader()
        writer.writerows(records)


def main():
    args = parse_args()
    records = sample_means(args.n, args.k_values, args.repeats)
    write_csv(records, args.output)
    print(f"Saved {len(records)} rows → {args.output}")


if __name__ == "__main__":
    main()
