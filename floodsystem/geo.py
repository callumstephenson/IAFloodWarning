# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
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
    distance_list = sorted_by_key(distance_list,1)
    return distance_list

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
    rivers = set()
    for n in stations:
        rivers.add(stations[n].river)
    return rivers
