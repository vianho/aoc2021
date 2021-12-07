from utils import get_logger
LOGGER = get_logger()

def get_gamma_rate(data):
    """
    get the most common bit of each datapoint.
    """
    num_of_data = len(data)
    num_of_bits = len(data[0])
    gamma_rate = [0] * num_of_bits
    for d in data:
        for i in range(num_of_bits):
            gamma_rate[i] += int(d[i])

    gamma_rate = [1 if x > num_of_data/2 else 0 for x in gamma_rate]
    gamma_rate = ''.join(map(str, gamma_rate))

    return gamma_rate
