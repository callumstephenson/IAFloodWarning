# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from operator import truediv
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    '''function returns a sorted list of stations and their distance from a coordinate p

    args:
        stations(list): list of MonitoringStation class objects
        p(tuple): tuple of coordinates (lon,lat)
    
    return:
        list of tuples sorted by descending distance from given coordinate p
    '''
    distance_list = []
    for each in stations:
        coord = each.coord
        dist = haversine(p,coord)
        distance_list.append((each,float(dist)))
    return sorted_by_key(distance_list,1)

def stations_within_radius(stations, centre, r):
    '''when given a list of stations, centre, and radius, this function outputs a list
    of stations within the given radius
    
    args:
        stations(list): list of MonitoringStation class objects
        centre(tuple): tuple of centre coordinates (lon,lat)
        radius(float): radius of circle
    
    return:
        list of stations within the given radius
    '''
    distance_list = stations_by_distance(stations, centre)
    within_radius = []
    for each in distance_list:
        if each[1] <= r:
            within_radius.append(each)
    return within_radius

def rivers_with_station(stations):
    '''when given a set of MonitoringStation objects, this function returns the name of the rivers
    with a monitoring station
    
    args:
        list of MonitoringStation objects
    
    return:
        set of rivers
    '''
    rivers = set()
    for each in stations:
        river_name = each.river
        rivers.add(river_name)
    return rivers

def stations_by_river(stations):
    '''when given a list of MonitoringStation objects, this function returns a dictionary
    of river:stations on river. 

    args:
        list of MonitoringStation objects
    
    return:
        dict of rivers:stations on river
    '''
    rivers = rivers_with_station(stations)
    river_stations = {river:[] for river in list(rivers)}
    for each in stations:
        river_stations[each.river].append(each.name)
    return river_stations

def rivers_by_station_number(stations, N):
    '''when given a list of MonitoringStation objects and Nth place in list
    functoin returns amount of rivers with number of stations >= Nth place

    args:
        stations: list of MonitoringStation objects
        N: Nth place in list
    
    returns:
        (name,number of stations) for all stations >= Nth place.
    '''
    river_stations = stations_by_river(stations)
    if N > len(river_stations):
        raise ValueError
    rivers_station_number = []
    for key in river_stations.keys():
        x = len(river_stations[key])
        rivers_station_number.append((key,x))
    rivers_station_number = sorted_by_key(rivers_station_number, 1, reverse=True)
    stations_above_n = []
    for each in rivers_station_number:
        if each[1] >= rivers_station_number[N][1]:
            stations_above_n.append(each)
    return stations_above_n
