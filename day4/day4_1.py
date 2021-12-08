from utils import get_logger
LOGGER = get_logger()
import numpy as np

def get_winning_bingo_board(sequence, boards):
    """
    Returns the score of the winning bingo board.
    """
    score = 0

    # idea: store the number of items crossed out in the row/column in a dictionary
    # and check if the number of items crossed out is equal to the number of items in the row/column

    # create a dictionary with the number of items crossed out in each row
    mark = '-1'
    for s in sequence:
        LOGGER.debug("Sequence: %s", s)
        for bidx, b in enumerate(boards):
            LOGGER.debug("=== Board no: %s ===", bidx)
            LOGGER.debug("Board: %s", b)
            for i, row in enumerate(b):
                LOGGER.debug("Row: %s", row)

                if s in row:
                    LOGGER.debug("Found %s in row %s", s, i)
                    col_idx = row.index(s)
                    row[col_idx] = mark
                    LOGGER.debug("row-changed: %s", row)
                    if check_row(row) or check_column(b, col_idx):
                        return calculate_score(b, bidx, s)
                    break

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
    LOGGER.info("Winning board: Board no. %s", board_index)
    pretty_print(board)
    LOGGER.info("Total: %s, Current: %s, Score: %s", sum(flat_board), called_number, score)
    return score

def pretty_print(board, printer=LOGGER.info):
    """
    Print the board.
    """
    printer(f"Board: \n{board[0]} \n{board[1]} \n{board[2]} \n{board[3]} \n{board[4]}")

