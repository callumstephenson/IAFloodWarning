import matplotlib 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from pygments import highlight
from floodsystem.analysis import polyfit




def plot_water_levels(station, dates, levels):
    '''creates a plot from MonitoringStation object, dates, levels (x,y). Plot of water level against date.

    args:
        station:  MonitoringStation object that the dates and levels are from
        dates = list of dates you want to plot
        levels = list of levels corresponding to dates
    '''
    # creating low and high lines
    typical_low_line = [station.typical_range[0]]*len(levels)
    typical_high_line = [station.typical_range[1]]*len(levels)
    # creating plot and labels
    plt.plot(dates, levels)
    plt.plot(dates, typical_low_line)
    plt.plot(dates, typical_high_line)
    plt.xlabel("date")
    plt.ylabel("water level (m)")
    plt.xticks(rotation=45)
    plt.title(station.name)
    # show plot
    plt.tight_layout()
    plt.show()
    
def plot_water_level_with_fit(station, dates, levels, p):
    
    poly, d0 = polyfit(dates,levels, p)
    time = date2num(dates)
    
    plt.plot(dates, levels, '.')
    x = np.linspace(time[0], time[-1], 30)
    plt.plot(x, poly(x - d0))
    
    plt.plot([min(dates), max(dates)], [station.typical_range[0], station.typical_range[0]], color='g', label="$Typical Low$")
    plt.plot([min(dates), max(dates)], [station.typical_range[1], station.typical_range[1]], color='r', label="$Typical High$")
    
    plt.title("{}".format(station.name))
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.legend(loc=2)
    plt.show()

