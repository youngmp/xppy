#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import json

# Add your imports here.
import numpy as np
import os
import pylab
#import yaml
import pdb


def lib(fin, fout, pars):
  try:
      os.remove(fout)
  except Exception as e:
      pass
  # plotting pars from yaml
  #with open(pars, 'r') as pars:
  #    pars = yaml.load(pars)
  aspect = pars["aspect"]
  vmax = pars["vmax"]
  vmin = pars["vmin"]
  #skip_col = 0
  #pdb.set_trace()
  dat = np.genfromtxt(fin,autostrip=True)
  if 'timeaxis' in pars and pars['timeaxis']:
    timeaxis = dat[:,0]
    dat = dat[:,1:]
    lentimeaxis = len(timeaxis)
    #pdb.set_trace()
    xticklocations = list(range(int(0), int(lentimeaxis), int(lentimeaxis/4)))
    xticklabels = ['{:.0f}'.format(i) for i in timeaxis[xticklocations]]
    #print vmin
    #pdb.set_trace()
    pylab.xticks(xticklocations, xticklabels)
  #dat = dat[:,skip_col:]
  #print dat
  pylab.imshow(np.transpose(dat),vmin=vmin,vmax=vmax,aspect=aspect);
  #pylab.show()
  pylab.savefig(fout,dpi=75)
  pylab.close("all")

def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', default=sys.stdin)
  parser.add_argument('-o', '--output')
  parser.add_argument('-p', dest='pars', type=json.loads)
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.output, args.pars)
  #lib(args.fin, args.ode)

if __name__=='__main__':
  main()

