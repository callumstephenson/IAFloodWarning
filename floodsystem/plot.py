import matplotlib.pyplot as plt
from .station import MonitoringStation
from .analysis import polyfit
import matplotlib


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
    """Display water level data alongside best-fit polynomial"""
    poly, offset = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    plt.plot(dates, poly(x - offset), label = "best fit")
    plot_water_levels(station, dates, levels)
    return
