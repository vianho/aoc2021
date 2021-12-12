from utils import get_logger
LOGGER = get_logger()
import numpy as np

def draw_horizontal_line(board, startx, endx, y):
    for col in range(startx, endx + 1):
        board[y][col] += 1
    return board

def draw_vertical_line(board, starty, endy, x):
    for row in range(starty, endy + 1):
        board[row][x] += 1
    return board

def draw_diagonal_line(board, coord1, coord2):
    # Get the coordinates
    x1, y1 = coord1
    x2, y2 = coord2

    # Get the direction
    x_dir = 1 if x2 > x1 else -1
    y_dir = 1 if y2 > y1 else -1
    
    # draw diagonal line
    for x, y in zip(range(x1, x2 + x_dir, x_dir), range(y1, y2 + y_dir, y_dir)):
        board[y][x] += 1

    return board

def calculate_points(board):
    """
    Calculate the number of items larger than 2
    """
    flat_board = np.array(board).flatten()
    return np.count_nonzero(flat_board > 1)

def pretty_print(board, title="Board", printer=LOGGER.info):
    """
    Print the board.
    """
    out = '\n'.join([str(row) for row in board])
    # printer(f"Board: \n{board[0]} \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")
    printer(f"{title}: \n{out}")
