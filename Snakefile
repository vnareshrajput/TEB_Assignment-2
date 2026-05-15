configfile: "config.yaml"

N       = config["n"]
K_VALS  = config["k_values"]
REPEATS = config["repeats"]

K_STR = " ".join(str(k) for k in K_VALS)


rule all:
    input:
        f"plots/lln_for_n_{N}.png"


rule simulate:
    output:
        "data/results.csv"
    shell:
        "python scripts/simulate.py "
        "--n {N} "
        "--repeats {REPEATS} "
        "--k_values {K_STR} "
        "--output {output}"


rule plot:
    input:
        "data/results.csv"
    output:
        f"plots/lln_for_n_{N}.png"
    shell:
        "python scripts/plot.py "
        "--input {input} "
        "--output {output} "
        "--n {N}"
