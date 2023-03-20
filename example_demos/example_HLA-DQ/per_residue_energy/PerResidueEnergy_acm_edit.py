#/usr/bin

import os
import sys

readFile = open(sys.argv[1],"r")

scoreHash = {}

for line in readFile:
    line = line.rstrip()
    fields = line.split()
    if (fields[0] != "--" and fields[1] != "--"):
        res1 = int(fields[0])
        res2 = int(fields[1])
        value = float(fields[2])
        key = str(res1)+" "+str(res2)

        if key in scoreHash:
            scoreHash[key] += value
        else:
            scoreHash[key] = value

pepEnergy = {}

for key in scoreHash:
    fields = key.split()
    res1 = int(fields[0])
    res2 = int(fields[1])
    newKey = str(res2)
    if res1 < 181:
        if newKey in pepEnergy:
            pepEnergy[newKey] += float(scoreHash[key])/3
        else:
            pepEnergy[newKey] = float(scoreHash[key])/3

for key in pepEnergy:
    print(key, pepEnergy[key])
