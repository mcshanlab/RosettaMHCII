#!/usr/bin/env python3

#   Base code by Santrupti Nerli Feb 2018 for MHCI
#   Updated by Andrew McShan Feb 2021 for MHCII

# Load the Rosetta commands for use in the Python shell
from pyrosetta import *

#import custom libraries for model, argparse and mhc databases
from model import MODEL
from input_output.input.argparser import ARGPARSE
from database.HLA_sequences_180 import hla_sequences_180
from database.mhciialpha import mhciialpha
from database.mhciibeta import mhciibeta

# import other required libraries
import os
import sys
import subprocess

'''

Main is the entry point of RosettaMHC

'''

# method to run the RosettaMHC protocol
def run():
    args = ARGPARSE()

    if args.is_list_mhcs() == True:
        if not args.is_no_trim_mhc_flag_set():
            for key,value in hla_sequences.items():
                print(key)
        else:
            for key,value in hla_sequences_180.items():
                print(key)

    else:
        # Load Rosetta database files
        init(options='')
        modeller = MODEL(args)
        modeller.model_mhc_for_each_peptide_beta2m_tcr_chaperone_mhciialpha_mhciibeta()

if __name__ == "__main__":
    run()
