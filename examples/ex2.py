"""
This file demonstrates how to modify an ode file and plot the output.
"""

from shutil import copyfile
import os
import matplotlib.pyplot as plt

import xppy

# run ode file, collect data (see ex1.py)
out1 = xppy.run('simple.ode')
dat1 = out1.getRawData()
desc1 = out1.getDesc()

t1 = dat1[:,desc1['t']]
u1 = dat1[:,desc1['u']]
v1 = dat1[:,desc1['v']]

# this feature is unimplemented, but you can hack around it.

# get this list by running
# readOdePars(ode_file)
# modify the entry you want.
# Let's change q from 1 to 10.
# and u from .2 to -.2
inputdat = [['par', 'q', '10'],
            ['init', 'u', '-.2'],
            ['init', 'v', '.5'],
            ['@', 'dt', '.01'],
            ['@', 'total', '100']]

# copy file to temporary file
copyfile('simple.ode','simple_temp.ode')

# modify the temporary file
xppy.parse.changeOde(inputdat,ode_file='simple_temp.ode')

# run the temporary file
out2 = xppy.run('simple_temp.ode')
dat2 = out2.getRawData()
desc2 = out2.getDesc()

# remove temporary file
#os.remove('simple_temp.ode')

t2 = dat2[:,desc2['t']]
u2 = dat2[:,desc2['u']]
v2 = dat2[:,desc2['v']]


# plot before change
fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.plot(u1,v1)

# plot after change
ax2 = fig.add_subplot(122)
ax2.plot(u2,v2)

plt.show()
