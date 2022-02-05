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

    Args:
        stations(list): List of MonitoringStation class objects
        p(tuple): Tuple of coordinates (lon,lat)
    
    Returns:
        list of tuples sorted by descending distance from given coordinate p
    '''
    x = []
    for each in stations:
        coord = each.coord
        dist = haversine(p,coord)
        x.append((each,float(dist)))
    x = sorted_by_key(x,1)
    return x