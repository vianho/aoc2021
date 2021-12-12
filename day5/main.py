from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day5_1 import hor_ver_only
from day5_2 import all_points

def process_data(input_data):
    return [tuple(tuple(int(i) for i in e.split(',')) for e in d.split('->')) for d in input_data]

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))
    LOGGER.info(f'{len(data)=}')
    LOGGER.info(f'{data[:10]=}')

    # preprocess data
    data = process_data(data)
    LOGGER.info(f'preprocessed_data[:10]={data[:10]}')

    # get maximum x and y
    max_x = max(max(coord[0] for coord in start_end) for start_end in data)
    max_y = max(max(coord[1] for coord in start_end) for start_end in data)
    LOGGER.info(f'{max_x=} {max_y=}')

    board = [[0] * (max_x + 1) for _ in range(max_y + 1)]

    # filter only horizontal or vertical lines
    hor_ver = list(filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], data))
    LOGGER.info(f'{len(hor_ver)=}')

    # diagonal lines
    diag = list(filter(lambda x: x not in hor_ver, data))
    LOGGER.info(f'{len(diag)=}')

    # part 1
    hor_ver_points_overlap, board = hor_ver_only(hor_ver, board)
    LOGGER.info(f'{hor_ver_points_overlap=}')

    # part 2
    all_points_overlap, _ = all_points(diag, board)
    LOGGER.info(f'{all_points_overlap=}')

if __name__ == '__main__':
    main()
