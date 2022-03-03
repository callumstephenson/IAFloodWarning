import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    N = 5
    highest_waterlevel_stations = stations_highest_rel_level(stations, N)
    dt = 10
    p = 4
    for station in highest_waterlevel_stations:
        try:
            measure_id = station.measure_id
            dates, levels = fetch_measure_levels(measure_id, datetime.timedelta(days=dt))
            plot_water_level_with_fit(station, dates, levels, p)
            
        except IndexError:
            pass

if __name__ == "__main__":
    run()