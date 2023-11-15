import subprocess

preamble ='''import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend([
'''

postamble='''])'''

folder = "/store/user/lpcdarkqcd/boosted/signal_production_1dscans_v01/MINIAOD"
cmd = lambda x,y: subprocess.check_output("eos root://cmseos.fnal.gov ls {} {}".format(x,y), shell=True).split('\n')

for signal in cmd("",folder):
    with open("../python/Private1DUL18/{}_cff.py".format(signal.replace("0.","0p")),'w') as sigfile:
        sigfile.write(preamble)
        path = folder+"/"+signal
        for file in cmd("-lh",path):
            if len(file)==0: continue
            if "0 Nov" in file: continue
            file = file.split(' ')[-1]
            sigfile.write("       '"+path+"/"+file+"',\n")
        sigfile.write(postamble)

