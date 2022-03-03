import matplotlib
import numpy as np
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    '''a function that given the water level time history for a station computes a least-squares fit of a polynomial of degree p to water level data. 

    args:
        dates:  list of dates 
        levels = list of levels of water
        p = degree of polynomial
    '''

    x = matplotlib.dates.date2num(dates)
    y = matplotlib.dates.date2num(levels)
    p_coeff = np.polyfit(x - x[0], y, p)
    poly = np.poly1d(p_coeff)
    plt.plot(x, y, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1 - x[0]))   
    plt.show()

def plot_water_level_with_fit(station, dates, levels, p):
    '''a function that plots the water level data and the best-fit polynomial. 

    args:
        station: a MonitoringStation object
        dates:  list of dates 
        levels = list of levels of water
        p = degree of polynomial
    '''
    for 
