"""
This file demonstrates how to extract parameter names and values, and variable names and values.
Currently, any variable line initialized with 'par, init, @' are considered parameters.
"""

import xppy
import matplotlib.pyplot as plt

# list all high level modules
modlist = dir(xppy)
print modlist

# run ode file, catch output using class Output.
out = xppy.Output('simple.ode')

# save raw data output to convenient name
dat = out.getRawData()

# read ODE variables
# output is a dictory of a 1-1 map of variables with corresponding index.
# for example, variable 't' has index 0. 
# call 0 to get the first state variable name, or call 't' to get its index.
desc = out.getDesc()
print desc

# the above is equivalent to
print xppy.readOdeVars('simple.ode')

# read ODE params
print xppy.readOdePars('simple.ode')

#-----------------------------------------------------------------------

# plot output
# only the column names need to be known to assign them to a dedicated variable
t = dat[:,desc['t']]
u = dat[:,desc['u']]
v = dat[:,desc['v']]

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(t,u)
ax.plot(t,v)
plt.show()

