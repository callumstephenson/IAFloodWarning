# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        d += "   latest level:  {}".format(self.latest_level)
        return d

    def typical_range_consistent(self):
        'Checking to see if MonitoringStation object has valid tuple as typical range'
        return type(self.typical_range) is tuple
    

    def relative_water_level(self):
        '''Takes self as argument (MonitoringStation object), returns a value ranging from 0.0 to 1.0 describing the latest water
        level relative to typical'''
        if (not self.typical_range_consistent()) or (self.latest_level == None):
            return None
        else:
            return (self.latest_level-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])

def inconsistent_typical_range_stations(stations):
    '''Given a list of MonitoringStation objects, returns a list of stations with inconsistent
    data for typical range

    args:
        station list of MonitoringStation objects
    
    return:
        list of MonitoringStation objects with inconsistent data
    '''
    inconsistent_stations = []
    for each in stations:
        if each.typical_range_consistent() == False:
            inconsistent_stations.append(each)
    return inconsistent_stations
    