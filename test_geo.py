from numpy import geomspace
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_by_station_number, rivers_with_station, stations_by_river
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from haversine import haversine

def test_stations_by_distance():
    '''Build list of 10 stations
    '''
    stations = build_station_list()
    selected_stations = stations[0:9]
    stations_distance = stations_by_distance(selected_stations, (52.2053, 0.1218))
    ''' check with a specific input
    '''
    assert stations_distance[0][0].name == 'Cambridge Jesus Lock'
    assert stations_distance[-1][0].name == 'Penberth'
    assert stations_distance[0][1] == 0.840237595667494
    ''' Check that the list is sorted by distance
    '''
    for i in range(len(stations_distance) - 1):
        assert stations_distance[i][2] < stations_distance[i+1][2]

def test_stations_within_radius():
    ''' Build list of stations within 10km of cambridge city centre
    '''
    stations = build_station_list()
    stations_radius = stations_within_radius(stations.build_station_list(), (52.2053, 0.1218), 10)
    ''' check with a specific input
    '''
    assert len(stations_radius) == 11
    ''' Check for all the elements
    '''
    for station in stations_radius:
        radius = haversine(station.coord, (52.2053, 0.1218))
        assert radius < 10

def test_rivers_with_station():
    ''' build station list
    '''
    stations = build_station_list()
    rivers = rivers_with_station(stations)
    ''' Check if the numbers of stations match expectation
    '''
    assert len(rivers) >= 900
    ''' check with a specific input
    '''
    assert "Addlestone Bourne" in rivers

def test_rivers_by_station_number():
    s_id = "test_s_id"
    m_id = "test_m_id"
    label = "station"
    coord = (1, 1)
    trange = None
    river1 = "River 1"
    river2 = "River 2"
    river3 = "River 3"
    town = "test_Town"
    station_1 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    station_2 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    station_3 = MonitoringStation(s_id, m_id, label, coord, trange, river1, town)
    station_4 = MonitoringStation(s_id, m_id, label, coord, trange, river3, town)
    station_5 = MonitoringStation(s_id, m_id, label, coord, trange, river2, town)
    stations = [station_1, station_2, station_3, station_4, station_5]

    assert len(rivers_by_station_number(stations, 1)) == 1

    river_list = rivers_by_station_number(stations, 2)

    # Multiple entries with same number in Nth position
    assert len(river_list) == 2

    assert "River 3" not in [item[0] for item in river_list]