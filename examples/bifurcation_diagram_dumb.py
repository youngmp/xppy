"""
messy example of how to use the bifurcation diagram function in xppy

in this data file, there are no stable periodic solutions. Only one stable fixed point that gives rise to a couple whacky unstable periodic solutions.

In read_diagram, the code does not take into account both hi-lo values, so you will only see half the bifurcation diagram if you started with hi-lo.

"""

import numpy as np
import matplotlib.pyplot as plt

#from xppy.utils import diagram
from xppy.utils import plot

# load data
filename = 'twodphs_cxs_hopf_diagram_q=1.dat'
raw_data = np.loadtxt(filename)

# clean data
data = diagram.read_diagram(raw_data)

# the output data is organized as follows.

# data[:,0] is the x-variable for all branches
# data[:,[1,5]] is the set of stable fixed points
# data[:,[2,6]] is the set of unstable fixed points
# data[:,[3,7]] is the set of stable periodic solutions
# data[:,[4,8]] is the set of unstable periodic solutions


fig = plt.figure()
ax = fig.add_subplot(111)

# plot stable fixed points
ax.scatter(data[:,0],data[:,1],s=10,color='red')
ax.scatter(data[:,0],data[:,5],s=10,color='red')

# plot unstable fixed points
ax.scatter(data[:,0],data[:,2],s=10,color='black')
ax.scatter(data[:,0],data[:,6],s=10,color='black')

# plot stable periodic solutions
ax.scatter(data[:,0],data[:,3],s=10,color='green')
ax.scatter(data[:,0],data[:,7],s=10,color='green')

# plot unstable periodic solutions
ax.scatter(data[:,0],data[:,4],s=10,color='blue')
ax.scatter(data[:,0],data[:,8],s=10,color='blue')

# a scatter plot is necessary for now because there are many discontinuous sets of data that matplotlib interprets as adjacent. Try running plot instead of scatter to see what I mean.

plt.show()


