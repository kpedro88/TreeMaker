#!/bin/bash

if [ "$1" == 1 ]
then 
    exit
fi

outputDir=$1
KEEPTAR=$2

./FScheck.sh "$KEEPTAR"

#### Spring15 rare backgrounds - single top
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1
python generateSubmission.py -n 1 -s -o $outputDir -c Spring15 -f Spring15.ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1
