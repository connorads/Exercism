""" Module for currency exchange. """


def exchange_money(budget: float, exchange_rate: float) -> float:
    """ Calculates the amount of foreign currency you can get for your money.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """ Calculates the amount of money you have left after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """ Calculates the total value of bills you have.

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget: float, denomination: int) -> int:
    """ Calculates the number of bills you can get for your money.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return int(budget // denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """ Calculates the amount of money you have left after exchanging.

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """

    return budget % denomination


def exchangeable_value(budget: float, exchange_rate: float, spread: int, denomination: int) -> int:
    """ Calculates the maximum value you can get for your money.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    exchange_rate_with_spread = exchange_rate * (1 + spread / 100)
    exchanged_value = exchange_money(budget, exchange_rate_with_spread)
    number_of_bills = get_number_of_bills(exchanged_value, denomination)
    return get_value_of_bills(denomination, number_of_bills)
