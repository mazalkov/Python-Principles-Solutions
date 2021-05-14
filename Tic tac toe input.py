# https://pythonprinciples.com/challenges/Tic-tac-toe-input/


def get_row_col(position):
    
    # I am aware that this is a terrible way to do it
    board = {
        "A1" : (0, 0),
        "A2" : (1, 0),
        "A3" : (2, 0),
        
        "B1" : (0, 1),
        "B2" : (1, 1),
        "B3" : (2, 1),
        
        "C1" : (0, 2),
        "C2" : (1, 2),
        "C3" : (2, 2),
    }
    
    return board.get(position)
