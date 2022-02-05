from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    stations = build_station_list()
    x = stations_within_radius(stations, (52.2053,0.1218), 10)
    y = [x[i][0].name for i in range(len(x))]
    print(y)
    return None

if __name__ == "__main__":
    run()