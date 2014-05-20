#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import json

# Add your imports here.
import numpy
import subprocess as sproc
import os
import yaml

def lib(fin, fout, fin2):
  try:
    os.remove(fout)
  except Exception as e:
    pass
  dat = numpy.genfromtxt(fin,autostrip=True)
  #growthrate = 1./(6.*134./20.)
  pars = yaml.load(open(fin2).read())
  #print pars
  #print pars["shiftfunction"]
  shiftfunction = lambda t: eval(pars["shiftfunction"])
  #shiftfunction = lambda t: numpy.round(1./(6.*134./20.)*t+20)
  #jS0position = lambda t: jtailbudposition(t) - 20
  t = dat[:,0]
  vals = dat[:,1:]
  shearvector = (numpy.shape(vals)[1])*numpy.ones(numpy.shape(dat)[0])-shiftfunction(t)
  res = shear(vals, shiftv=shearvector, axis=pars["shiftaxis"])
  outdat = numpy.column_stack((t,res))
  numpy.savetxt(fout, outdat,delimiter=' ')

def shear(a, shiftv=None, axis=0):
  """
  See numpy roll.
  The difference is that it takes a vector to define the shift
  >>> x = numpy.reshape(numpy.arange(20), (4,5))
>>> print x
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
>>> shiftv = numpy.array([0,1,3,2])
>>> print shiftv
[0 1 3 2]
>>> print shear(x, shiftv, 0)
[[ 0  1  2  3  4]
 [ 9  5  6  7  8]
 [12 13 14 10 11]
 [18 19 15 16 17]]
>>>
  """
  res = numpy.empty_like(a)
  for i,shift in enumerate(shiftv):
    #pdb.set_trace()
    if axis==0:
      res[i,:] = numpy.roll(a[i,:], int(shift))
    elif axis==1:
      res[:,i] = numpy.roll(a[:,i], int(shift))
  return res


def create_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--input', help="", default=sys.stdin)
  parser.add_argument('-o', '--output')
  parser.add_argument('-y', dest='yaml')
  return parser

def main():
  parser = create_parser()
  args = parser.parse_args()
  lib(args.input, args.output, args.yaml)
  #lib(args.fin, args.ode)

if __name__=='__main__':
  main()

