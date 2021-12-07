from utils import get_logger
LOGGER = get_logger()

def manual_distance(data):
    """
    Calculate the closest distance from the current position to end position based on the submarine manual.
    """
    x, y = 0, 0
    aim = y
    for d in data:
        direction, distance = d.split()
        distance = int(distance)

        if direction == 'down':
            aim += distance
        elif direction == 'up':
            aim -= distance

        if direction == 'forward':
            x += distance
            y += distance * aim
        LOGGER.debug(f'{x=}, {y=}, {aim=}, {d=}')
    return x * y
