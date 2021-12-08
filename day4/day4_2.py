from day4_utils import check_row, check_column, calculate_score, pretty_print
from utils import get_logger
LOGGER = get_logger()

def get_losing_bingo_board(sequence, boards):
    """
    Returns the score of the winning bingo board.
    """
    board_status = [0] * len(boards)

    mark = '-1'
    for s in sequence:
        LOGGER.debug("Sequence: %s", s)
        for bidx, status in enumerate(board_status):
            LOGGER.debug("=== Board no: %s - status: %s ===", bidx, status)
            if status == 1:
                continue

            curr_board = boards[bidx]

            pretty_print(curr_board, printer=LOGGER.debug)

            for i, row in enumerate(curr_board):
                LOGGER.debug("Row: %s", row)
                if s in row:
                    LOGGER.debug("Found %s in row %s", s, i)
                    col_idx = row.index(s)
                    row[col_idx] = mark
                    LOGGER.debug("row-changed: %s", row)
                    if check_row(row) or check_column(curr_board, col_idx):
                        LOGGER.debug("Board %s is crossed out", bidx)
                        pretty_print(curr_board, printer=LOGGER.debug)
                        board_status[bidx] = 1
                        if board_status == [1] * len(board_status):
                            return calculate_score(curr_board, bidx, s)
                        continue
