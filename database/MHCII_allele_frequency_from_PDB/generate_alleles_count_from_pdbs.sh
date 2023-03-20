#!/bin/bash

awk '{print $1}' mhciialpha.txt | sort | uniq -c | sort -nk2  > mhciialpha_counts_for_histogram.txt

awk '{print $1}' mhciibeta.txt | sort | uniq -c | sort -nk2  > mhciibeta_counts_for_histogram.txt