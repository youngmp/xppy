#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""This module does blah blah."""

import argparse
import sys


import os
#from jinja2 import Environment,FileSystemLoader,Template
from jinja2 import Template
import xppy
#import pickle
import yaml
import pdb
import json

import os,inspect
thisdir=os.path.dirname(os.path.realpath(inspect.getfile(inspect.currentframe())))

def lib(fin, modelpars, ode, dat):
  """This function simulates jinjaxpp into a dat file

  :param foo: The input is jinjaxpp
  :returns: the output is a dat file
  """
  dat = os.path.join(os.getcwd(),dat)
  ode = os.path.join(os.getcwd(),ode)
  #pass
  try:
    os.remove(fout)
  except Exception as e:
    pass
  tmpl = Template(fin.read())
  #print jinjavar
  outode = tmpl.render(yaml.load(modelpars))
  #print ode,outode
  with open(ode, 'w') as fode: 
    fode.write(outode)
  #ode = os.path.join(thisdir,ode)  
  #print ode
  o = xppy.run(ode_file=ode, output_file=dat)  

def create_parser():
  parser = argparse.ArgumentParser(description='jinjaxpp.py -i model.jn -y modelpars.yml --ode output.ode --dat output.dat  -p \'{"nx" : 4, "ny" : 4}\'')
  parser.add_argument('-i', '--input', help='model.jn to substitute with yaml vars', type = argparse.FileType('r'), default=sys.stdin)
  parser.add_argument('-y', dest="modelpars", type=argparse.FileType('r'), help='YML file to substitute in model')
  parser.add_argument('--ode', default='output.ode', help='model.ode for use with simulation software XPPAUT')
  parser.add_argument('--dat', default='output.dat', help='model.data simulation result from XPPAUT')
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.modelpars, args.ode, args.dat)
  #lib(args.fin, args.ode)

if __name__=='__main__':
  main()

