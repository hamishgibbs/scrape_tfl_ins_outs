import os
import pandas as pd
from glob import glob

types = ["ins", "outs", "taps"]
stations = [os.path.basename(x).split(".")[0] for x in glob("data/tfl_daily/ins/raw/*.json")]

rule all:
    input: 
        "data/tfl_daily/qa_success.txt",
        "rulegraph.svg"

rule clean_daily:
    input:
        "src/clean_daily.py",
        "data/tfl_daily/{type}/raw/{station}.json"
    output:
        "data/tfl_daily/{type}/clean/{station}.csv"
    shell:
        "python {input} {output}"

rule combine_daily:
    input:
        "src/combine_daily.py",
        expand("data/tfl_daily/{type}/clean/{station}.csv", type=types, station=stations)
    output:
        "data/tfl_daily/tfl_data.csv"
    shell:
        "python {input} {output}"

rule qa_daily:
    input:
        "src/qa_daily.py",
        "data/tfl_daily/tfl_data.csv"
    output:
        "data/tfl_daily/qa_success.txt"
    shell:
        "python -m pytest {input[0]} -vv --fn {input[1]} | tee {output}"

rule rulegraph:
    input:
        "Snakefile"
    output:
        "rulegraph.svg"
    shell:
        "snakemake --rulegraph | dot -Tsvg > {output}"