#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys


import os
#from jinja2 import Environment,FileSystemLoader,Template
#from jinja2 import Template
#import xppy
#import pickle
import yaml
import pdb
import json
import numpy as np

import os,inspect
thisdir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))

def lib(fninfpath, fnoutfpath, yml):
  argsyaml = yaml.load(open(yml).read())
  matin = np.genfromtxt(fninfpath, delimiter=' ')
  positionx = argsyaml['positionx']
  positiony = argsyaml['positiony']
  sizex = argsyaml['sizex']
  sizey = argsyaml['sizey']
  matout = matin[positionx:positionx+sizex, positiony:positiony+sizey]
  np.savetxt(fnoutfpath, matout, delimiter=' ')

def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', help='NPZ simulation file', default=sys.stdin)
  parser.add_argument('-o', '--output', help='DAT 3D simulation file', default=sys.stdout)
  parser.add_argument('-y', dest='yml', help='parameters')
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.output, args.yml)

if __name__=='__main__':
  main()

