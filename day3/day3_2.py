from utils import get_logger
LOGGER = get_logger()

def get_o2_gen_rating(data):
    num_of_bits = len(data[0])
    bitcount = [0] * num_of_bits
    keep = data

    for i in range(num_of_bits):
        for k in keep:
            bitcount[i] += int(k[i])        

        most_common = '1' if bitcount[i] >= len(keep)/2 else '0'
        LOGGER.debug(f"bitcount[{i}] = {bitcount[i]}")
        keep = [k for k in keep if k[i] == most_common]

        LOGGER.debug(f'{len(keep)=}')
    LOGGER.debug(f'{keep=}')
    return keep[0]

def get_co2_scrub_rating(data):
    num_of_bits = len(data[0])
    bitcount = [0] * num_of_bits
    keep = data

    for i in range(num_of_bits):
        if len(keep) == 1:
            break
        for k in keep:
            bitcount[i] += int(k[i])        

        least_common = '0' if bitcount[i] >= len(keep)/2 else '1'
        LOGGER.debug(f"bitcount[{i}] = {bitcount[i]}")
        keep = [k for k in keep if k[i] == least_common]

        LOGGER.debug(f'{len(keep)=}')
    LOGGER.debug(f'{keep=}')
    return keep[0]

