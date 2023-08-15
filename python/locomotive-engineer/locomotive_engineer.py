"""Functions which helps the locomotive engineer to keep track of the train."""


from typing import TypedDict


def get_list_of_wagons(*wagons: int) -> list[int]:
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Fix the list of wagons.

    :parm each_wagons_id: list - the list of wagons.
    :parm missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    w_a, w_b, w_1, *rest_wagons = each_wagons_id
    return [w_1, *missing_wagons, *rest_wagons, w_a, w_b]


Route1 = TypedDict("Route1", {"from": str, "to": str})
Route2 = TypedDict("Route2", {"from": str, "to": str, "stops": list[str]})


def add_missing_stops(route: Route1, **stops: str) -> Route2:
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """

    return {
        **route,
        "stops": list(stops.values()),
    }


MoreRouteInfo = TypedDict("MoreRouteInfo", {"length": str, "speed": str})
Route3 = TypedDict("Route3", {"from": str, "to": str, "length": str, "speed": str})


def extend_route_information(
    route: Route1, more_route_information: MoreRouteInfo
) -> Route3:
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    return {
        **route,
        **more_route_information,
    }


WagonRowList = list[list[tuple[int, str]]]


def fix_wagon_depot(wagons_rows: WagonRowList) -> WagonRowList:
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """

    colour_1, colour_2, colour_3 = wagons_rows

    return [
        [colour_1[0], colour_2[0], colour_3[0]],
        [colour_1[1], colour_2[1], colour_3[1]],
        [colour_1[2], colour_2[2], colour_3[2]],
    ]
