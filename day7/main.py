from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day7_1 import least_steps_required
from day7_2 import least_fuel_required

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))

    data = list(map(int, data[0].split(',')))

    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')
    
    least_steps = least_steps_required(data)
    LOGGER.info(f'{least_steps=}')

    least_fuel = least_fuel_required(data)
    LOGGER.info(f'{least_fuel=}')

if __name__ == '__main__':
    main()
