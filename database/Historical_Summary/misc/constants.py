#       Sgourakis Lab
#   Author: Sagar Gupta
#   Date: May 24, 2022
#   Email: sagar@sas.upenn.edu

import string

# parameters
MUTATION_THRESH = 5 # number of allowed mutations in the HLA (inclusive)

LONG_PEP_LENGTH = 30 # Upper bound on what we consider a "peptide" chain
PEP_LOWER = 8 # Smallest peptide length to consider
PEP_UPPER = 25 # Longest peptide length to consider

MHCIIALPHA_CUTOFF = 50 # Sequence identity score cutoff for MHC II alpha chain
MHCIIBETA_CUTOFF = 50 # Sequence identity score cutoff for MHC II beta chain

RECEPTOR_DIST = 5 # Distance (Å) threshold between peptide and receptor

DISTANCE_PEP_MHC = 15.0 # 65th residue of MHC Ca atom and 2nd residue for peptide Ca atom (from observation)

MHC_TRIM_LENGTH = 181 # Number of residues in MHC chain + 1 (so really it is 180)

FIRST_MHC_STRUC_YEAR = 1988

alphabet_string = string.ascii_uppercase

ALPHABET = list(alphabet_string)

# reference values
# DRA101 and DRB101
MHCIIALPHA_SEQ = "EHVIIQAEFYLNPDQSGEFMFDFDGDEIFHVDMAKKETVWRLEEFGRFASFEAQGALANIAVDKANLEIMTKRSNYTPITNVPPEVTVLTNSPVELREPNVLICFIDKFTPPVVNVTWLRNGKPVTTGVSETVFLPREDHLFRKFHYLPFLPSTEDVYDCRVEHWGLDEPLLKHWEFD"
MHCIIBETA_SEQ = "DTRPRFLWQLKFECHFFNGTERVRLLERCIYNQEESVRFDSDVGEYRAVTELGRPDAEYWNSQKDLLEQRRAAVDTYCRHNYGVGESFTVQRRVEPKVTVYPSKTQPLQHHNLLVCSVSGFYPGSIEVRWFRNGQEEKAGVVSTGLIQNGDWTFQTLVMLETVPRSGEVYTCQVEHPSVTSPLTVEWRA"

MHCII_MOTIFS = {'DRA': 'EHV', 'DPA': 'AGA', 'DQA': 'DHV',
                'DRB': 'DTR', 'DPB': 'ATP', 'DQB': 'EGR'}

DEFAULT_MHCIIALPHA_CHAIN = 'A'
DEFAULT_MHCIIBETA_CHAIN = 'B'
DEFAULT_PEP_CHAIN = 'C'

DRA_MOTIF = 'EHV'
DRB_MOTIF = 'DTR'
DPA_MOTIF = 'AGA'
DPB_MOTIF = 'ATP'
DQA_MOTIF = 'DHV'
DQB_MOTIF = 'EGR'

DATABASE_SCRIPT_PATH = "/Volumes/8TB_McShan_Drive/RosettaMHCII/database/Historical_Summary/"
ROSETTA_INSTALL_DIR = "~/Desktop/rosetta.source.release-314/"
