# Written by Andrew McShan
# Contact: andrew.mcshan@chemistry.gatech.edu

# usage: python3 extract_mhciialpha_sequences.py > mhciialpha.txt

import os
import sys

from Bio import SeqIO

for seq_record in SeqIO.parse("hla_prot_mhcii_only.fasta", "fasta"):
    if (
        len(seq_record.seq) >=250):
        mhciisequences = seq_record.description.split()[1]
        mhciialpha = ["DMA", "DOA", "DPA", "DQA", "DRA"]
        mhcfulllength = seq_record.seq
        mhciicutstart = mhcfulllength[28:]
        mhciicutend = mhciicutstart[:-48]
        if any(
               x in mhciisequences for x in mhciialpha):
                print("mhciialpha['HLA-"+seq_record.description.split()[1]+"']='"+mhciicutend+"'")
