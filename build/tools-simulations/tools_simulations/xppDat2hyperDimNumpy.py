#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys


import os
#from jinja2 import Environment,FileSystemLoader,Template
#from jinja2 import Template
#import xppy
#import pickle
#import yaml
import pdb
import json
import numpy as np

import os,inspect
thisdir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))

def lib(fin, fout, pars):
  nx = pars['nx']
  ny = pars['ny']
  nbvar = pars['nbvar']
  dat=np.loadtxt(fin)
  t= dat[:,0]
  dat = dat[:,1:] 
  dat2 = np.empty((len(t),nx,ny,nbvar))
  dati = 0
  for space2i in range(ny):
    for space1i in range(nx):
      for vari in range(nbvar):
        dat2[:,space1i,space2i,vari] = dat[:,dati]
        dati = dati + 1
  np.savez(fout ,dat2, t)

def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', default=sys.stdin)
  parser.add_argument('-o', '--output', default=sys.stdout)
  parser.add_argument('-p', dest='pars', type=json.loads)
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.output, args.pars)
  #lib(args.fin, args.ode)

if __name__=='__main__':
  main()

