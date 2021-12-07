from utils import get_logger
LOGGER = get_logger()

def count_increased_w1(data):
    """
    Count the number of times the data is increased by a window of 1.
    """
    increased = 0
    prev = data[0]

    for d in data:
        if d > prev:
            increased += 1
        LOGGER.debug(f'{prev=} - {d=} - {d > prev=} - {increased=}')
        prev = d
    
    return increased
