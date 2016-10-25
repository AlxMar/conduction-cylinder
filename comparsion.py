import numpy as np
import scipy.special as spec
import matplotlib
matplotlib.use("Agg")
from matplotlib import rc
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
import matplotlib.pyplot as plt
from boutdata import collect

T = np.squeeze(collect("T", path="data1", xguards=False))
#dr = collect("dr", path="data")
dz = collect("dz", path="data1", xguards=False)
#print 'dz = ', dz
#print 'dr.sum , len(dr)    ',dr.sum(), len(dr)
#print 'dr = ', dr
#sum = 0
#for i in range(32):
#    sum = sum + dx[i+2] 
#print 'real dx sum = ', sum
print T.shape
time = collect("t_array", path="data1")


lenr = len(T[0,:,0])
lenz = len(T[0,0,:])




#sum = np.zeros(len(time))
#for i in range(len(time)):
#	for j in range(lenx):
#		for k in range(lenz):
#			sum[i] = sum[i] + T[i,j,0,k]

Rmax = 1.8
Rmin = 0.05

dr = (Rmax - Rmin) / lenr
print dr, lenr, dr*32

### Analytical solution
A2k = [2.51, 1.02, 0.64, 0.49, 0.39, 0.32, 0.28, 0.24, 0.22, 0.2, 0.18, 0.16, 0.15, 0.14, 0.13, 0.12, 0.12, 0.11, 0.1, 0.1]
B2k = spec.jnp_zeros(2, 20)


Tan = np.zeros((len(time),lenr,lenz))

#for k in range(20):
#   Tan = Tan + A2k[k]*J2(B2k[k]*r/rmax)*exp(-B2k[k]**2/rmax**2*time)

for i in range(len(time)):
    for j in range(lenr):
        r = (j+1)*dr
        for l in range(lenz):
            theta = (l+1)*dz
            for k in range(20):
                Tan[i,j,l] = Tan[i,j,l] + A2k[k]*spec.jv(2, B2k[k]*r/Rmax).real*np.cos(2*theta)*np.exp(-B2k[k]**2/Rmax**2*time[i])



#for i in range(lenr):
#    T[:,i,:] = np.sqrt(T[:,i,:])

plt.plot(time, T[:,63,64], 'bo', label="BOUT++")
plt.plot(time, Tan[:,63,64], 'r', label = "Analytical")
plt.legend(loc=2)
plt.title(r"$r_0 = 1.8, \phi_0 = \pi/2$")
plt.xlabel(r"$t$")
plt.ylabel(r"$T(t,r_0,\phi_0)$")
plt.grid()
#plt.show()
plt.savefig("results1/cmpr-3.png")
print "Success!"
#plt.axis([0,2,-1e-6,1e-6])
#plt.show()

