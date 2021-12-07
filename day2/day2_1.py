from utils import get_logger
LOGGER = get_logger()

def closest_distance(data):
    """
    Calculate the closest distance from the current position to end position.
    """
    x, y = 0, 0
    for d in data:
        direction, distance = d.split()
        distance = int(distance)
        y = y + (1 if direction == 'down' else (-1 if direction == 'up' else 0)) * distance
        x = x + distance if direction == 'forward' else x
        LOGGER.debug(f'{x=}, {y=}, {d=}')
    return x * y
