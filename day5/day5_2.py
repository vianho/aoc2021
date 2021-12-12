from utils import get_logger
LOGGER = get_logger()
from day5_utils import pretty_print, calculate_points, draw_diagonal_line

def all_points(data, board):
    # get board from the horizontal & vertical part
    for start, end in data:
        LOGGER.debug(f'{start} -> {end}')
        draw_diagonal_line(board, start, end)
    
    pretty_print(board, "Final board", LOGGER.debug)

    return calculate_points(board), board
