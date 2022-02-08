from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def run():
    stations = build_station_list()
    x = stations_by_river(stations)
    for each in x.values():
        each.sort()
    print(x["River Aire"]) , print(x["River Cam"]) , print(x["River Thames"])
    return None

if __name__ == '__main__':
    run()
