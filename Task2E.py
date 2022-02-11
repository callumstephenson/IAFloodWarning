from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)
    y = stations_highest_rel_level(stations, 5)
    for each in y:
        dates, levels = fetch_measure_levels(each.measure_id,
                                        dt=datetime.timedelta(days=10))
        plot_water_levels(each, dates, levels)


if __name__ == "__main__":
    run()