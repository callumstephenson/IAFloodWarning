from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np
import datetime
import matplotlib.dates

def run():
    risk_severe = []
    risk_high = []
    risk_moderate = []
    risk_low = []
    not_applicable = []
    stations = build_station_list()
    update_water_levels(stations)
    for each in stations:
        if each.typical_range_consistent() and each.latest_level is not None:
            percentage = each.relative_water_level(each.latest_level)
            if percentage > 1.6:
                risk_severe.append(each.name)
            elif percentage > 1.2:
                risk_high.append(each.name)
            elif percentage > 0.8:
                risk_moderate.append(each.name)
            else:
                risk_low.append(each.name)
        else:
            not_applicable.append(each.name)
        if each.name in risk_high:
            try:
                measure_id = each.measure_id
                dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=5))
                bestfit, offset = polyfit(dates, levels, p=4)
                derivative = np.polyder(bestfit)
                gradient = derivative(matplotlib.dates.date2num(dates[0]) - offset)
                if gradient > 1:
                    risk_high.remove(each.name)
                    risk_severe.append(each.name)
            except IndexError:
                pass
            except KeyError:
                pass
    
    risk_severe.sort()
    risk_high.sort()
    risk_moderate.sort()
    risk_low.sort()
    not_applicable .sort()
    print(f"Severe Risk:\n{risk_severe}\n")
    print(f"High Risk:\n{risk_high}\n")
    print(f"Moderate Risk:\n{risk_moderate}\n")
    print(f"Low Risk:\n{len(risk_low)} stations\n")
    print(f"No Reliable Data:\n{len(not_applicable)} stations\n")

if __name__ == "__main__":
    run()