#   Sgourakis Lab
#   Author: Sagar Gupta
#   Date: May 24, 2022
#   Email: sagarg@sas.upenn.edu

# import required libraries
import argparse
import csv
import os
from collections import defaultdict

# import custom libraries
from misc.fasta import FASTA
from misc.constants import *

def historical():

    fasta = FASTA(f"{DATABASE_SCRIPT_PATH}/PDBS_new.fasta")
    fasta.read()
    pdb_dict_year = fasta.get_pdb_dict_year()


    with open(f"{DATABASE_SCRIPT_PATH}/historical_summary.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["year", "per_year", "cumulative_sum"])
        year_sum = defaultdict(list)
        cumulative_sum = defaultdict(int)

        year_min = min(list(pdb_dict_year.values()))
        year_max = max(list(pdb_dict_year.values()))
        for pdbid, year in pdb_dict_year.items():
            year_sum[year].append(pdbid)

        cumulative = 0

        for year in range(year_min, year_max + 1):
            cumulative += len(year_sum[year])
            writer.writerow([year, len(year_sum[year]), cumulative])
            cumulative_sum[year] = cumulative
            year_sum[year] = len(year_sum[year])

    print(f"Min year {year_min} and Max year {year_max} and total structures {cumulative}")

if __name__ == "__main__":

    historical()
