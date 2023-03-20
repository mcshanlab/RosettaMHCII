#!/bin/bash

# step 1

for filename in ../*_relaxed_*.pdb; do
name=`basename $filename .pdb`
pdb=".pdb"
fullname=$name$pdb
  echo $fullname
  residue_energy_breakdown.static.macosclangrelease -in:file:s ../"$fullname" -out:file:silent "$name"_per_residue_energy_breakdown.out  -ignore_unrecognized_res
done;

wait $!

# step 2

for filename in *_per_residue_energy_breakdown.out; do
nocut=`basename $filename`
name=`basename $filename _per_residue_energy_breakdown.out`
txt=".txt"
fullname="$name"_per_residue_energy_breakdown_peptide_only.txt
echo $no
echo $nocut
awk '{print $3, $6, $28}' "$nocut" > "$fullname"_awk_step2.txt
done;

wait $!

for filename in *_awk_step2.txt; do
nocut=`basename $filename`
name=`basename $filename _awk_step2.txt`
echo $name
awk 'FNR > 1 {print $1, $2, $3}' "$nocut" > "$name"_awk_step3.txt
done;

wait $!

# step 4

for filename in *_awk_step3.txt; do
nocut=`basename $filename`
name=`basename $filename _awk_step3.txt`
echo $name
python PerResidueEnergy_acm_edit.py "$nocut" > "$name"_python_per_residue_peptide_energy_graph.txt
done;

wait $!

# step 5

for filename in *_python_per_residue_peptide_energy_graph.txt; do
nocut=`basename $filename`
name=`basename $filename _python_per_residue_peptide_energy_graph.txt`
echo "$name"
sort -k1 -n "$nocut" > "$name"_sorted.txt
done;

wait $!

# step 6

for filename in *_sorted.txt; do
nocut=`basename $filename`
name=`basename $filename _sorted.txt`
peptidelength=16
echo "$peptidelength"
echo "$name"
tail -n "$peptidelength" "$nocut" > "$name"_mer_extracted_peptide_only_graphy.txt
done;

wait $!

# step 7

for filename in *_mer_extracted_peptide_only_graphy.txt; do
nocut=`basename $filename`
name=`basename $filename _mer_extracted_peptide_only_graphy.txt`
echo "$nocut"
echo "set term postscript color solid
set boxwidth 0.5
unset key
set xlabel \"Peptide Residue\"
set ylabel \"Energy\"
set linetype 1 lc rgb \"black\"
set yrange [-5:1]
set output \""$name"mer.eps\"
set style fill solid
plot \""$nocut"\" using 1:(\$2) with boxes" > "$name"_gnuplot.gnu
done;

wait $!

# step 8

for filename in *_gnuplot.gnu; do
nocut=`basename $filename`
name=`basename $filename _gnuplot.gnu`
echo "$name"
gnuplot "$name"_gnuplot.gnu
done;

wait $!

# remove all the unncessary files

rm *.out
rm *_awk_step2.txt
rm *_awk_step3.txt
rm *_python_per_residue_peptide_energy_graph.txt
rm *_sorted.txt
rm *.gnu
