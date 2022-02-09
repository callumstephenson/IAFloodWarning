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
