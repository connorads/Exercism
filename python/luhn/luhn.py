"""Luhn is a simple checksum formula used to validate a variety of identification
   numbers such as credit card numbers and Canadian Social Insurance Numbers."""


class Luhn:
    """Luhn algorithm implementation."""

    def __init__(self, card_num: str):
        """Initialize the card number."""
        self.card_num = card_num.replace(" ", "")

    def valid(self) -> bool:
        """Return True if the card number is valid, False otherwise."""
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False
        card_digits = [int(digit) for digit in self.card_num]
        card_digits.reverse()
        for second_digit in range(1, len(card_digits), 2):
            card_digits[second_digit] *= 2
            if card_digits[second_digit] > 9:
                card_digits[second_digit] -= 9
        return sum(card_digits) % 10 == 0
