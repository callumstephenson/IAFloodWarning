<<<<<<< HEAD
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    names = []
    for i in range(len(inconsistent)):
        inconsistent[i] = inconsistent[i].name
    inconsistent.sort()
    print(inconsistent)
    return None

if __name__ == "__main__":
    run()
=======
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    stations = build_station_list()
    inconsistent = inconsistent_typical_range_stations(stations)
    inconsistent.sort()
    print(inconsistent)
    return None

if __name__ == "__main__":
    run()
>>>>>>> aca3281531aadc1992e9fb3c6d4e6163d176e4b7
