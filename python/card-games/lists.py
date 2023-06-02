"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

from typing import List


def get_rounds(number: int) -> List[int]:
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number, number + 1, number + 2]


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand: List[int]) -> float:
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand: List[int]) -> bool:
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    mean = card_average(hand)
    return mean in ((hand[0] + hand[-1]) / 2, hand[len(hand) // 2])


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    odds = [hand[odd_index] for odd_index in range(1, len(hand), 2)]
    evens = [hand[even_index] for even_index in range(0, len(hand), 2)]
    return card_average(evens) == card_average(odds)


def maybe_double_last(hand: List[int]) -> List[int]:
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_card = hand[-1]
    rest_of_hand = hand[:-1]
    return rest_of_hand + [last_card * 2] if last_card == 11 else hand
