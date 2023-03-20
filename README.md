***** RosettaMHCII setup and installation on MacOS. Linux installation may require additional / different libraries. *****  

At the time of testing MacOS Monterey v12.4

•    Install Xcode for Mac

Visit the MacOS App Store

Search for Xcode

Download and install Xcode 

{at the time of testing Xcode v13.4.1)

•    Install Anaconda

Go to https://www.anaconda.com/products/distribution 

Download the latest anaconda distribution

Then 

conda create --name myenv

y

conda activate myenv

*Note that myenv should be active throughout the rest of the installation processes described below.  
You can set conda activate myenv in your .login and .cshrc / .bashrc file so it runs in default for every terminal you open.

•    Install pymol and biopython

conda install -c schrodinger pymol

conda install -c conda-forge biopython

•    Install Rosetta

Go to https://www.rosettacommons.org/software/license-and-download

Request an Academic License (Start Here)

Then Academic Download

Download Rosetta 3.13 (Tuesday, June 1, 2021)

Rosetta 3.13 source - as one bundle (5.2G)

{At time of testing Rosetta 3.13}

tar -xvzf rosetta[releasenumber].tar.gz

cd rosetta*/main/source

./scons.py -j 8 mode=release bin

After, add path to Rosetta to .cshrc or .bashrc

For more instructions on how to install Rosetta please see https://new.rosettacommons.org/demos/latest/tutorials/install_build/install_build 

*Note if there is a security issue go to System Preferences > Security & Privacy > Allow the file

•    Install PyRosetta

Obtain Rosetta license from to receive a username and password.

Download the appropriate version of PyRosetta
https://www.pyrosetta.org/downloads 

{at time of testing PyRosetta4.Release.python38.mac.release-321.tar.bz2}

tar -vjxf PyRosetta4.Release.python38.mac.release-321.tar.bz2

cd PyRosetta4.Release.python38.mac.release-321

cd setup && sudo python setup.py install

python3

import pyrosetta; pyrosetta.init()

*Note if there is a security issue go to System Preferences > Security & Privacy > Allow the file rosetta.so

•    Install ClustalOmega

Go to http://www.clustal.org/omega/ 

Under Precompiled binaries 
download Standalone Mac binary (PowerPC/64-bit Intel) (1.2.3)

mv clustal-omega-1.2.3-macosx clustalo

chmod u+x clustalo

*Note if there is a security issue go to System Preferences > Security & Privacy > Allow the file clustalo

{at time of testing clustalo 1.2.3}

•    Install gnuplot

gnuplot is used for plotting purposes

conda install -c conda-forge libgd 

then

conda install -c conda-forge gnuplot

{at time of testing gnuplot Version 5.4 patchlevel 3}

***** Example Run ***** 

See the "example_demos" folder for example runs for HLA-DR, HLA-DQ, and HLA-DP complexes.

Each folder should contain the following files:

- run.sh
This file contains all the commands needed to run RosettaMHCII. 
The commands in these files have been tailored for each allele class because the length of the allele sequences are different:

* For HLA-DR

for filename in *.pdb;do

name=`basename $filename`

python3 ../../main.py -template_pdb "$name" -nstruct 3 -relax_after_threading -mhciialpha mhciialpha_list -mhciibeta mhciibeta_list -peptides pep_list -mhciialpha_chain A -mhciibeta_chain B -peptide_chain C -no_trim_mhc -pep_start_index 368 -interface_cutpoint 367 -groove_distance 10

done


* For HLA-DQ


for filename in *.pdb;do

name=`basename $filename`

python3 ../../main.py -template_pdb "$name" -nstruct 3 -relax_after_threading -mhciialpha mhciialpha_list -mhciibeta mhciibeta_list -peptides pep_list -mhciialpha_chain A -mhciibeta_chain B -peptide_chain C -no_trim_mhc -pep_start_index 364 -interface_cutpoint 363 -groove_distance 10

done



* For HLA-DP


for filename in *.pdb;do

name=`basename $filename`

python3 ../../main.py -template_pdb "$name" -nstruct 3 -relax_after_threading -mhciialpha mhciialpha_list -mhciibeta mhciibeta_list -peptides pep_list -mhciialpha_chain A -mhciibeta_chain B -peptide_chain C -no_trim_mhc -pep_start_index 366 -interface_cutpoint 365 -groove_distance 10

done


- template PDB
This file is the PDB template used by RosettaMHCII for modeling.
You will find curated templates in the database/PDBs folder. Each of these files has been manually curated for accuracy of the program (modeled missing residues, fixed chain IDs, etc).

Important note for use of templates:
You MUST use a PDB template with the same HLA class (DR, DP, DQ), peptide length (i.e., 13mer), peptide binding register (i.e., reg3) as the peptide / HLA complex you want to model. If this condition is not met, modeling will not be accurate.
One PDB template should be sufficient for modeling of most problems. However, you may compare multiple templates in the run.sh script with a command to grab all available templates corresponding to your allele class and binding register:

cp ../../database/PDBs/*DR-13mer-reg3*.pdb .

- pep_list
The file provides a list of the peptide(s) you want to model in FASTA format.
example:
>PKYVKQNTLKLAT
PKYVKQNTLKLAT

- mhciialpha_list
This file provides the name of the class II HLA alpha chain allele to be modeled.
example:
HLA-DRA*01:01:01:01

Note that a list of all available HLA alpha chain alleles are listed in databases/mhciialpha.py
If the allele you want to model is not listed there, you can add it manually but it must be the same length as the other alleles in that class (DR, DQ, DP).

- mhciibeta_list
This file provides the name of the class II HLA beta chain allele to be modeled
example:
HLA-DRB1*01:01:01:01

Note that all available HLA alpha chain alleles are listed in databases/mhciibeta.py
If the allele you want to model is not listed there, you can add it manually but it must be the same length as the other alleles in that class (DR, DQ, DP).

- clean.sh
This file will clean the folder and allow you to restart the run.

***** Expected Outputs ***** 

- *_relaxed_0.pdb
This file is the RosettaII model, which has been relaxed. 

- binding_energies.csv
This file should contain a list of Interface Energies (in Rosetta Energy Units) for each of the modeled peptide/HLA complexes.
Lower energy means better predicted peptide/HLA binding.

- Additional Analysis: Per Residue Energy

see the per_residue_energy folder for a script to analysis the Per Residue Energy of each peptide/HLA interaction.
Look for patterns of low energy at the P1, P4, and P9 positions. This indicates a strong likelihood the peptide is a true binder.
