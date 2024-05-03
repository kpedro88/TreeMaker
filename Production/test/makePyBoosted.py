import os,sys
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from Condor.Production.jobSubmitter import generalized_ls

def checkSlash(args,attrs):
    for attr in attrs:
        arg = getattr(args,attr)
        if arg[-1]!='/': setattr(args,attr,arg+'/')

def doPy(args,sample):
    files = generalized_ls(args.redir,sample)
    name = os.path.basename(sample)
    with open(args.output+name.replace('.','p')+"_cff.py",'w') as outfile:
        outfile.write("import FWCore.ParameterSet.Config as cms\n\n")
        outfile.write("maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )\n")
        outfile.write("readFiles = cms.untracked.vstring()\n")
        outfile.write("secFiles = cms.untracked.vstring()\n")
        outfile.write("source = cms.Source (\"PoolSource\",fileNames = readFiles, secondaryFileNames = secFiles)\n")
        counter = 0
        # split into chunks of 255
        for ifile,file in enumerate(files):
            if counter==0: outfile.write("readFiles.extend( [\n")
            outfile.write("       '"+file+"',\n")
            if counter==254 or ifile==len(files)-1:
                outfile.write("] )\n")
                counter = 0
            else:
                counter += 1

if __name__=="__main__":
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--dir", dest="dir", type=str, required=True, help="sample directory")
    parser.add_argument("-x", "--redir", dest="redir", type=str, default="root://cmseos.fnal.gov/", help="sample directory")
    parser.add_argument("-o", "--output", dest="output", type=str, required=True, help="output directory")
    args = parser.parse_args()

    checkSlash(args,['dir','redir','output'])

    samples = generalized_ls(args.redir,args.dir+"MINIAOD")
    for sample in samples:
	    doPy(args,sample)
