#!/bin/bash

DIR=/store/user/lpcdarkqcd/boosted/signal_production_1dscans_v01/MINIAOD
for signal in $(eos root://cmseos.fnal.gov/ ls $DIR); do
#	echo ${DIR}/${signal} 
#	eos root://cmseos.fnal.gov ls -lh ${DIR}/${signal} | grep "0 Nov"
	echo $signal
	signal2=$(echo $signal | sed 's/0\./0p/')
	cmsRun xsecfinder_cfg.py name=Private1DUL18.${signal2} redir=root://cmseos.fnal.gov/ numevents=-1 >& xsec_${signal2}.log
done
