"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time: int):
    """Calculate the remaining bake time.

    Function that takes the time already spent baking the lasagna and returns
    the number of minutes to wait before the lasagna is ready.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int):
    """Calculate the preparation time.

    Function that takes the number of layers you want to add to the lasagna
    and returns how many minutes you would spend making them.
    """

    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int):
    """Calculate the elapsed time.

    Function that takes the number of layers you want to add to the lasagna,
    and the number of minutes the lasagna has been in the oven, and returns
    the total number of minutes you've worked on cooking the lasagna.
    """

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
