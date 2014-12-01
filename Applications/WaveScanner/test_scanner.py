# test_scanner.py [data_array] ===> visualization, error_metric, json
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import expresso_api as exp
import scanner
import sliceImage
import sys


def func(x, b, c, d):
    return 1 * np.cos(b * x - c) + d

""" VISUALIZATION FUNCTIONS """

def error(x, wave):
    popt, pcov = curve_fit(func, x, wave)
    print "cos(bx -c) + d: ", popt, "\ncovariance", pcov
    return popt, pcov

def plot(x, expected, observed):
    plt.figure()
    plt.plot(x, expected, 'k-', label="Expected", linewidth=5)
    plt.plot(x, observed, 'b-', label="Observed")
    

    # popt, pcov = error(x, observed)

    # plt.plot(x, func(x, *popt), 'r-',label="Fitted Curve") #
    plt.legend()
    plt.show()

def log_wave(name, wave):
    # name = 'pyramid'
    # wave = [0, 1, 2, 3, 4, 3, 2, 1, 0]
    exp.send_behavior(name, wave)

def print_wave(x, expected):
    baseLine = np.zeros(len(x))
    baseLine.fill(-1)
    midLine = np.zeros(len(x))
    plt.figure()
    plt.axis("off")
    plt.plot(x, expected, 'k-', label="Expected", linewidth=3)
    plt.plot(x, baseLine, 'k-', label="baseLine", linewidth=3)
    plt.plot(x, midLine, 'k-', label="midLine", linewidth=3)
    # plt.legend()
    plt.show()


""" EXAMPLE USAGE """
# x = np.linspace(0, 6 * np.pi,50)
# y = func(x, 1, 0, 0)
# y = y / np.max(y)
# yn = y + 0.2 * np.random.normal(size=len(x))

# PLOT WAVES, CALCULATE ERROR
# plot(x, y, yn)
# print_wave(x, y)


def main(argv):
    if len(argv) != 1:
        print 'Please Specify an image.'
        exit(1)
    videoName = argv[0].split(".")[0]+".avi"
    pts = sliceImage.sliceImage(argv[0], videoName)
    # scan = scanner.Scanner(videoName)
    # pts = scan.get_wave()
    x = np.linspace(0, 6 * np.pi, len(pts))
    y = func(x, 1, 0, 1)
    y = y / np.max(y)
    print pts
    print len(pts), len(x), len(y)
    plot(x,y,pts)


if __name__ == "__main__":
    main(sys.argv[1:])