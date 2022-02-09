from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river, rivers_with_station

def run():
    stations = build_station_list()
    y = list(rivers_with_station(stations))
    y.sort()
    print(y[:10])
    x = stations_by_river(stations)
    for each in x.values():
        each.sort()
    print(x["River Aire"]) , print(x["River Cam"]) , print(x["River Thames"])
    print(len(x))
    return None

if __name__ == '__main__':
    run()
