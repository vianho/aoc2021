from utils import read_file, transform_input, get_logger
LOGGER = get_logger(level="INFO")
from day4_1 import get_winning_bingo_board
from day4_2 import get_losing_bingo_board

def main():
    filename = 'input.txt'
    data = transform_input(read_file(filename))
    LOGGER.info(f'{len(data)=}')
    LOGGER.debug(f'{data[:10]=}')

    # sequence of numbers to be called
    seq = data[0].split(',')
    boards = []
    board = []

    # create 2d list of boards for the bingo boards provided 
    for d in data[2:]:
        if d != '':
            board.append(d.split())

        if len(board) == 5:
            LOGGER.debug(f'{board=}')
            boards.append(board)
            board = []
            continue

    LOGGER.info(f'{len(boards)=}')

    # get the winning bingo board
    winning_board_score = get_winning_bingo_board(seq, boards)
    LOGGER.info(f'{winning_board_score=}')
    print()
    losing_board_score = get_losing_bingo_board(seq, boards)
    LOGGER.info(f'{losing_board_score=}')


if __name__ == '__main__':
    main()
