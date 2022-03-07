from floodsystem.datafetcher import fetch_measure_levels 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations_highest_rel_level(stations, 5)
    
    for each in station:
        dates, levels = fetch_measure_levels(each.measure_id, dt=datetime.timedelta(days=2))
        plot_water_level_with_fit(each, dates, levels, 4)
    
if __name__ == "__main__":
    run()
