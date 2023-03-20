#!/bin/bash

# Modify the *DP-17mer-reg3* line based on your desired peptide length and binding register. Uncomment if you want to use multiple templates.

# cp ../../database/PDBs/*DP-17mer-reg3*.pdb .

for filename in *.pdb;do

name=`basename $filename`

python3 ../../main.py -template_pdb "$name" -nstruct 3 -relax_after_threading -mhciialpha mhciialpha_list -mhciibeta mhciibeta_list -peptides pep_list -mhciialpha_chain A -mhciibeta_chain B -peptide_chain C -no_trim_mhc -pep_start_index 366 -interface_cutpoint 365 -groove_distance 10

done

awk -F "," '{print $8, $9}' binding_energies.csv | sort -nk2 | head -5 > top5_energy.txt
