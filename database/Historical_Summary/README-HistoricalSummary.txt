Purpose: This will create a graph of the total number of pMHC-II pdbs vs year.



*** Edit lines 49 and 50 of /RosettaMHCII/database/Historical_Summary/misc/constants.py ***

DATABASE_SCRIPT_PATH = "/Volumes/8TB_McShan_Drive/RosettaMHCII/database/Historical_Summary/"
ROSETTA_INSTALL_DIR = "~/Desktop/rosetta.source.release-314/"


*** Execute historical_summary.py ***

python3 historical_summary.py




*** Edit /RosettaMHCII/database/Historical_Summary/historical_summary.R line 4 and line 8 ***

tag = "/Volumes/8TB_McShan_Drive/RosettaMHCII/database/Historical_Summary/historical_summary"

TOTAL_STRUC = 160


*** Plot the data using R *** 

Rscript historical_summary.R

mv Rplots.pdf historical_summary.pdf



