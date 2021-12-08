from day4_utils import check_row, check_column, calculate_score
from utils import get_logger
LOGGER = get_logger()

def get_winning_bingo_board(sequence, boards):
    """
    Returns the score of the winning bingo board.
    """
    # idea: store the number of items crossed out in the row/column in a dictionary
    # and check if the number of items crossed out is equal to the number of items in the row/column

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
