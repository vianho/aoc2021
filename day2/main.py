from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")

from day2_1 import closest_distance
from day2_2 import manual_distance

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))
    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')

    dist1 = closest_distance(data)
    LOGGER.info(f'{dist1=}')

    dist2 = manual_distance(data)
    LOGGER.info(f'{dist2=}')

if __name__ == '__main__':
    main()
