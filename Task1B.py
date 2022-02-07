from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    x = stations_by_distance(stations,(52.2053,0.1218))
    y = [(station[0].name,station[0].town,station[1]) for station in x]
    print(y[:10]) , print(y[-10:])
    return None

if __name__ == "__main__":
    run()
