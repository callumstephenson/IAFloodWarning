import matplotlib
import datetime
from floodsystem.stationdata import build_station_list, update_water_levels 
from floodsystem.flood import stations_highest_rel_level
from matplotlib.dates import date2num
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def predicted_water_level(station, prediction):
    return (prediction - station.typical_range[0]) / (station.typical_range[1] - station.typical_range[0])

def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 20)
    target_stations = []
    for each in station:
        dates, levels = fetch_measure_levels(each.measure_id, dt=datetime.timedelta(days=2))
        if len(dates) < 1 or len(levels) < 1:
            continue
        poly, d0 = polyfit(dates, levels, 4)
        time = date2num(dates)
        current = max(time - d0)
        prediction = poly(current + 1)
        rise = predicted_water_level(each, prediction) - each.relative_water_level()
        if predicted_water_level(each, prediction) > each.relative_water_level():
            target_stations.append([each.name, rise])
            print("{}:\n\tRelative water level: {}\n\tPredicted relative water level: {}\n\tRise: {}".format(
                each.name, each.relative_water_level(), predicted_water_level(each, prediction), rise))
    target_towns = []
    for i, stations_risk in enumerate(target_stations):
        if stations_risk[0] in [towns for towns, count in target_towns]:
            target_towns[i][1] += stations_risk[1]
        else:
            target_towns.append(stations_risk[:])
    print('List of towns and the estimated flood risk:')
    print(target_towns)
    ratings = ['low', 'moderate', 'high', 'severe']
    for town, risk in target_towns:
        rating_factor = 0  
        if risk > 0.5:
            rating_factor = 1  
        if risk > 5:
            rating_factor = 2  
        if risk > 10:
            rating_factor = 3  
        print('{}:\n\t{}'.format(town, ratings[rating_factor]))
        
if __name__ == "__main__":
    run()