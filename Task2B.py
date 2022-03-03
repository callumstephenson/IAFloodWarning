from floodsystem.flood import stations_level_over_threshold # noqa
from floodsystem.stationdata import build_station_list, update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    x = stations_level_over_threshold(stations, 0.8)
    for each in x:
        print(each[0].name, each[1])
    return None


if __name__ == "__main__":
    run()