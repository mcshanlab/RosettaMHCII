#!/bin/bash

python3 ../../main.py -template_pdb *.pdb -nstruct 3 -relax_after_threading -mhciialpha mhciialpha_list -mhciibeta mhciibeta_list -peptides pep_list -mhciialpha_chain A -mhciibeta_chain B -peptide_chain C -no_trim_mhc -pep_start_index 364 -interface_cutpoint 363 -groove_distance 10
