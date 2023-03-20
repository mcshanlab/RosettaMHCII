#!/Users/sgourakislab/anaconda3/bin/python3

#usage: python extract_mhciibeta_sequences.py > mhciibeta.txt

import os
import sys

from Bio import SeqIO


for seq_record in SeqIO.parse("hla_prot_mhcii_only.fasta", "fasta"):
    if (
        len(seq_record.seq) >=250):
        mhciisequences = seq_record.description.split()[1]
        mhciibeta = ["DMB", "DOB", "DPB", "DQB","DRB"]
        mhcfulllength = seq_record.seq
        mhciicutstart = mhcfulllength[30:]
        mhciicutend = mhciicutstart[:-47]
        if any(
               x in mhciisequences for x in mhciibeta):
                print("mhciibeta['HLA-"+seq_record.description.split()[1]+"']='"+mhciicutend+"'")