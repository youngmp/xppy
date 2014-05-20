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

def lib(fninfpath, fnoutfpath):
  npzfile = np.load(fninfpath)
  t, arr = npzfile[npzfile.files[0]], npzfile[npzfile.files[1]]
  try:
    os.remove(fnoutfpath)
  except Exception as e:
    pass
  #
  outarr=arr[:,0,:,0]
  t2 = np.reshape(t,(len(t),1))
  outarr = np.concatenate((t2,outarr),axis=1)
  np.savetxt(fnoutfpath, outarr, delimiter=" ")

def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', help='NPZ simulation file', default=sys.stdin)
  parser.add_argument('-o', '--output', help='DAT 3D simulation file', default=sys.stdout)
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.output)

if __name__=='__main__':
  main()

