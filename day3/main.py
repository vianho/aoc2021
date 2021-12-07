from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day3_1 import get_gamma_rate
from day3_2 import get_co2_scrub_rating, get_o2_gen_rating

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))
    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')

    gamma_rate = get_gamma_rate(data)
    epsilon_rate = [1 if int(g) == 0 else 0 for g in gamma_rate]
    epsilon_rate = ''.join(map(str, epsilon_rate))
    power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
    LOGGER.info(f'{gamma_rate=} - {epsilon_rate=} - {power_consumption=}')


    # o2 generator rate
    o2_gen_rate = get_o2_gen_rating(data)
    co2_scrub_rate = get_co2_scrub_rating(data)
    life_support_rating = int(o2_gen_rate, 2) * int(co2_scrub_rate, 2)
    LOGGER.info(f'{o2_gen_rate=} - {co2_scrub_rate=} - {life_support_rating=}')    


if __name__ == '__main__':
    main()
