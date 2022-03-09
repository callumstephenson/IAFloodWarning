# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations   
import floodsystem.flood as flood



def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_inconsistent_typical_range_stations():

    s_id = "test_s_id"
    m_id = "test_m_id"
    label = "test_station"
    coord = (-2.0, 4.0)
    river = "test_river"
    town = "test_town"
    test_1 = None
    test_2 = (4, 2)
    test_3 = (1, 3)
    s1 = MonitoringStation(s_id, m_id, label, coord, test_1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, test_2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, test_3, river, town)

    stations = [s1, s2, s3]
    test_data = inconsistent_typical_range_stations(stations)
    assert s1 in test_data
    assert s2 in test_data
    assert s3 in test_data

