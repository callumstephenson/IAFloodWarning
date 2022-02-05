# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from haversine import haversine, Unit
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    x = []
    for each in stations:
        coord = each.coord
        dist = haversine(p,coord)
        x.append((each,float(dist)))
    x = sorted_by_key(x,1)
    return x