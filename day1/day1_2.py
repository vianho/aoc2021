from day1.day1_1 import LOGGER
from utils import get_logger
LOGGER = get_logger()

def count_increased_w3(data):
    """
    Count the number of times the data is increased by a window of 3.
    """
    increased = 0
    w = 3
    prev = sum(data[0:w])

    for i in range(len(data)):
        if i >= len(data) - w + 1:
            LOGGER.debug(f'{i=} {len(data)=}')
            break
        s = sum(data[i:i+w])
        if s > prev and i > 0:
            increased += 1
        LOGGER.debug(f'{prev=} - {s=} - {s > prev=} - {increased=}')
        prev = s
    
    return increased
