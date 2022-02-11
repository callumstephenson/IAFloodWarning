from floodsystem.stationdata import build_station_list , update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    x = [(each.name, each.relative_water_level()) for each in stations_highest_rel_level(stations, 10)]
    print(x)
    return None


if __name__ == "__main__":
    run()