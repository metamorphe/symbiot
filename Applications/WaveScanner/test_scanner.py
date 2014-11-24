# test_scanner.py [data_array] ===> visualization, error_metric, json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import expresso_api as exp



def func(x, b, c, d):
	return 1 * np.cos(b * x - c) + d

""" VISUALIZATION FUNCTIONS """

def error(wave):
	popt, pcov = curve_fit(func, x, wave)
	print "cos(bx -c) + d: ", popt, "\ncovariance", pcov
	return popt, pcov

def plot(x, expected, observed):
	plt.figure()
	plt.plot(x, expected, 'k-', label="Expected", linewidth=5)
	plt.plot(x, observed, 'b-', label="Observed")
	

	popt, pcov = error(observed)

	plt.plot(x, func(x, *popt), 'r-',label="Fitted Curve") #
	plt.legend()
	plt.show()

def log_wave(name, wave):
	# name = 'pyramid'
	# wave = [0, 1, 2, 3, 4, 3, 2, 1, 0]
	exp.send_behavior(name, wave)



""" EXAMPLE USAGE """
x = np.linspace(0, 6 * np.pi,50)
y = func(x, 1, 0, 0)
y = y / np.max(y)
yn = y + 0.2 * np.random.normal(size=len(x))

# PLOT WAVES, CALCULATE ERROR
plot(x, y, yn)
