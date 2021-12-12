from utils import get_logger
LOGGER = get_logger()

def least_steps_required(data):
    """
    Calculate the least fuel required to move the crab submarines to a specific position
    """

    median = sorted(data)[len(data)//2]
    LOGGER.info(f"{median=}")

    fuel_required = 0

    for position in data:
        fuel_required += abs(position - median)

    return fuel_required
