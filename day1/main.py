from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day1_1 import count_increased_w1
from day1_2 import count_increased_w3

def main():
    filename = "input.txt"
    data = transform_input(read_file(filename))
    LOGGER.info(f"{len(data)=}")

    # can also turn it into 1 function with window as a param, but i'm lazy :kek:
    increased1 = count_increased_w1(data)
    LOGGER.info(f"Numbers of time increased by window of 1: {increased1}")

    increased3 = count_increased_w3(data)
    LOGGER.info(f"Numbers of time increased by window of 3: {increased3}")

if __name__ == "__main__":
    main()
