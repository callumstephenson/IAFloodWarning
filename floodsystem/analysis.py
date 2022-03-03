import matplotlib.dates
import numpy as np

def polyfit(dates, levels, p):
    ''' Convert dates from datetime objects to a list of floats
    '''
    x = matplotlib.dates.date2num(dates)
    p_coeff = np.polyfit(x - x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return poly, x[0]