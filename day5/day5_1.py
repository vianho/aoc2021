from utils import get_logger
LOGGER = get_logger()
from day5_utils import pretty_print, draw_vertical_line, draw_horizontal_line, calculate_points

def hor_ver_only(data, board):
    for ((x1, y1), (x2, y2)) in data:
        LOGGER.debug(f'{(x1,y1)=} {(x2,y2)=}')
        if x1 == x2:
            # vertical line
            starty = min(y1, y2)
            endy = max(y1, y2)
            board = draw_vertical_line(board, starty, endy, x1)
        elif y1 == y2:
            # horizontal line
            startx = min(x1, x2)
            endx = max(x1, x2)
            board = draw_horizontal_line(board, startx, endx, y1)
    
    pretty_print(board, "Final board", LOGGER.debug)

    return calculate_points(board), board
