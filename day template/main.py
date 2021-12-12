from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="DEBUG")
# from dayx_1 import sol1
# from dayx_2 import sol2

def main():
    filename = 'test.txt'
    data = transform_input(read_file(filename))
    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')

if __name__ == '__main__':
    main()
