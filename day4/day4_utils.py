from utils import get_logger
LOGGER = get_logger()
import numpy as np

def check_row(row, mark='-1'):
    """
    Check if the rows are crossed out.
    """
    return row == [mark] * 5

def check_column(board, column_idx, mark='-1'):
    """
    Check if the columns are crossed out.
    """
    col = [row[column_idx] for row in board]
    return col == [mark] * 5

def calculate_score(board, board_index, called_number):
    """
    Calculate the score of the board.
    """
    flat_board = [0 if x < 0 else x for x in list(map(int, np.array(board).flatten()))]
    score = sum(flat_board) * int(called_number)
    # LOG the stats
    LOGGER.info("Losing board: Board no. %s", board_index)
    pretty_print(board, printer=LOGGER.info)
    LOGGER.info("Total: %s, Current: %s, Score: %s", sum(flat_board), called_number, score)
    return score

def pretty_print(board, printer=LOGGER.info):
    """
    Print the board.
    """
    printer(f"Board: \n{board[0]} \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")
