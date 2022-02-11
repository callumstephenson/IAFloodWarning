from .utils import sorted_by_key  # noqa
from .station import MonitoringStation # noqa


def stations_level_over_threshold(stations, tol):
    '''takes arguments MonitoringStation object list, tolerance and outputs a list of stations that are over the set tolerance

    args:
        stations = list of MonitoringStation objects, tolerance of relative water level you would like to check
    
    return:
        list of tuples [(MonitoringStation, MonitoringStation.relative_water_level)...] sorted descending by relative water level
    '''
    return_list = [(each, each.relative_water_level()) for each in stations if not each.relative_water_level() == None and each.relative_water_level() > tol]
    return sorted_by_key(return_list, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    '''takes arguments MonitoringStation objects, number of objects and outputs a list of the N highest stations sorted descending by relative water level

    args:
        stations = list of MonitoringStation objects, N = highest N stations you would like returned

    return:
        list of MonitoringStation objects, sorted descending for water level up until the Nth in the list
    '''
    relative_level_list = [(each, each.relative_water_level()) for each in stations if not each.relative_water_level() == None]
    return [each[0] for each in sorted_by_key(relative_level_list, 1, reverse=True)[:N]]

