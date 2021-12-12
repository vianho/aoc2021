import math
from utils import get_logger
LOGGER = get_logger()
from functools import lru_cache


def least_fuel_required(data):
    """
    Calculate the least fuel required to move the crab submarines to a specific position
    """

    average = sum(data)//len(data)
    LOGGER.info(f"floored {average=}")

    fuel_required = 0

    for position in data:
        LOGGER.debug(f"{position=} - fuel required: {triangular_sequence(abs(position-average))}")
        fuel_required += triangular_sequence(abs(position - average))
    return fuel_required

def triangular_sequence(n):
    """
    Calculate the triangular sequence
    """
    return int(n * (n+1) / 2)