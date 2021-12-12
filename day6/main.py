from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day6 import lanternfish_count

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))
    data = list(map(int, data[0].split(',')))
    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')

    after_80_days = lanternfish_count(data, 80)
    LOGGER.info(f'{after_80_days=}')

    after_256_days = lanternfish_count(data, 256)
    LOGGER.info(f'{after_256_days=}')

if __name__ == '__main__':
    main()
