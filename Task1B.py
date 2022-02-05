from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    stations = build_station_list()
    x = stations_by_distance(stations,(52.2053,0.1218))
    y = [(x[i][0].name,x[i][0].town,x[i][1]) for i in range(len(x))]
    print(y[:10]) , print(y[-10:])
    return None

if __name__ == "__main__":
    run()
