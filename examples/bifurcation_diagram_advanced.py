"""
In-progress more elegant example of how to plot bifurcation diagrams.

(Feb 2, 2017): xppy is currently incompatible with bifurcation data output from xpp version 8. So this example will not work until we go in and fix xppy.

"""

import numpy as np
import matplotlib.pyplot as plt

#from xppy.utils import diagram
from xppy.utils import plot

# load data
filename = 'twodphs_sxs_osc2_diagram_q=.125_all.dat'

fig = plt.figure()
ax = fig.add_subplot(111)

plot.plotDiag(filename,ax)
plt.show()
