#from pylab import *
import numpy as np
from time import sleep
import matplotlib
matplotlib.use("Agg")
from matplotlib import rc
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True

import matplotlib.pyplot as plt
#matplotlib.use("Agg")
#import matplotlib.animation as animation
from boutdata import collect
from boututils import DataFile

pathname = "data3"

T = np.squeeze(collect("T", path=pathname, xguards=False))
time = np.squeeze(collect("t_array", path=pathname, xguards=False))
#dx = collect(("dx", path="data")
#dz = collect("dz", path="data")
print T.shape
#dx = dx.squeeze()
#print dx

#time = collect("t", path="data")

#create 5000 Random points distributed within the circle radius 100
max_r = 1.8
min_r = 0.05
max_theta = 2.0 * np.pi
#number_points = 5000
#points = np.random.rand(number_points,2)*[max_r,max_theta]

#Some function to generate values for these points, 
#this could be values = np.random.rand(number_points)
#values = points[:,0] * np.sin(points[:,1])* np.cos(points[:,1])

#now we create a grid of values, interpolated from our random sample above
theta = np.linspace(0.0, max_theta, 128)
r = np.linspace(min_r, max_r, 64)
#grid_r, grid_theta = np.meshgrid(r, theta)
#data = griddata(points, values, (grid_r, grid_theta), method='cubic',fill_value=0)

#Create a polar projection


fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')
ax.set_axis_bgcolor('black')
ax.set_xticklabels([''])
ax.set_yticklabels([''])
#plt.show()
cax = ax.pcolormesh(theta,r, T[0,:,:])
fig.patch.set_facecolor('black')
color_bar = plt.colorbar(cax, orientation='horizontal')
cbytick_obj = plt.getp(color_bar.ax.axes, 'xticklabels')
plt.setp(cbytick_obj, color = 'white')

#cax = ax.pcolormesh(theta,r, T[i,:,0,:])


for i in range(len(time)):
    #Color bar
    txt = ax.text(0.9*np.pi,3., r'$t = ' + str(time[i]) + r'$', color='white', fontsize=16)
    #Plottingi
    cax.set_array(T[i,:-1,:-1].ravel())
    fig.savefig("pic/tempBR%0.5i.png" %i, facecolor=fig.get_facecolor(), edgecolor='none')
    txt.remove()
    #fig.clear()
