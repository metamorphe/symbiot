from pylab import *
from scipy.optimize import curve_fit

x = np.array([399.75, 989.25, 1578.75, 2168.25, 2757.75, 3347.25, 3936.75, 4526.25, 5115.75, 5705.25])
y = np.array([109,62,39,13,10,4,2,0,1,2])

#create and export an array of all of the x-values
#same with y-values

def func(x, a, b, c, d):
    return a*np.exp(-c*(x-b))+d

popt, pcov = curve_fit(func, x, y, [100,400,0.001,0])
print popt

x=linspace(400,6000,5) # (smallest x-value, largest x-value, #points)
plot(x,func(x,*popt))
show()


