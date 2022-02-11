from .utils import sorted_by_key  # noqa
from .station import MonitoringStation # noqa


def stations_level_over_threshold(stations, tol):
    return_list = [(each, each.relative_water_level()) for each in stations if not each.relative_water_level() == None and each.relative_water_level() > tol]
    return sorted_by_key(return_list, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    relative_level_list = [(each, each.relative_water_level()) for each in stations if not each.relative_water_level() == None]
    return [each[0] for each in sorted_by_key(relative_level_list, 1, reverse=True)[:N]]

