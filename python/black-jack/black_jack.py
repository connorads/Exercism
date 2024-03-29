"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

from typing import Literal


Card = Literal['A', '2', '3', '4', '5',
               '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def value_of_card(card: Card, ace_value: Literal[1, 11] = 1) -> int:
    """Determine the scoring value of a card.

    :param card: Card - given card.
    :param ace_value: int - value of ace card.  Default is 1.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return ace_value
    return int(card)


def higher_card(card_one: Card, card_two: Card) -> Card | tuple[Card, Card]:
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: Card - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    if (one_value := value_of_card(card_one)) > (two_value := value_of_card(card_two)):
        return card_one
    if two_value > one_value: 
        return card_two
    return (card_one, card_two)


def value_of_ace(card_one: Card, card_two: Card) -> int:
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: Card - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    return 11 if value_of_card(card_one, 11) + value_of_card(card_two, 11) <= 10 else 1


def is_blackjack(card_one: Card, card_two: Card) -> bool:
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: Card - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    return card_one == 'A' and value_of_card(card_two) == 10 or card_two == 'A' and value_of_card(card_one) == 10


def can_split_pairs(card_one: Card, card_two: Card) -> bool:
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: Card - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: Card, card_two: Card):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: Card - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    return 9 <= value_of_card(card_one) + value_of_card(card_two) <= 11
