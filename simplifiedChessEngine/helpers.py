
#region Parameters for board
ROWS = 4
COLUMNS = 4
player = [0, 1] ## Black and White
empty = [0][0]

#endregion

#region Parameters for pieces
# I am opting to use numerical values to indicate the pieces: 
# Odd for white and Even for black

# White
queen_W = 1
knight_W = 3
bishop_W = 5
rook_W = 7

# Black
queen_B = 2
knight_B = 4
bishop_B = 6
rook_B = 8


#endregion

def within_limits(row, column):
    """
    Determine if a given row is within the board limits
    
    returns: True if within limits, false otherwise
    """
    return ((row >= 0 and row < ROWS) and (column >= 0 and column < COLUMNS))


def valid_move(board_state, row, column, player=0):
    """
    Checks if a move ending is within limits and whether it is occupied 
    by an opponent or empty
    """
    return ((within_limits(row, column) 
            and board_state[row][column] == empty) or 
            (board_state[row][column] != empty and 
             board_state[row][column] % 2 != player))