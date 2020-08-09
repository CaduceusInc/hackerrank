import numpy as np

def initialize_pieces(config):
    """
    Takes the inputs: whites or blacks and initialises players
    """
    pieces = list()

    for piece_config in config:
        if piece_config[0] == 'Q':
            pieces.append(Queen(piece_config[1] + piece_config[2], ))
        elif piece_config[0] == 'R':
            pieces.append(Rook(piece_config[1] + piece_config[2]))
        elif piece_config[0] == 'K':
            pieces.append(Knight(piece_config[1] + piece_config[2]))
        else:
            pieces.append(Bishop(piece_config[1] + piece_config[2]))

class Pieces:
    def __init__(self, position, colour='White'):
        self.position = position
        self.colour = colour
        
    def return_possible_moves(self):
        pass
        
        
        
class Board:
    def __init__(self, whites, blacks, squares=4):
        self.squares=self.squares
        self.mat = np.zeros((squares, squares))
        
    
     

        
    def piece_state(self, piece, state):
        """
        Keep track of the state of the piece on the game board
        """
        self.piece = piece
        self.state = state
        
        return self.state, self.piece
    
    def process_move(self, move, player):
        """
        Process move and return new board config
        """

        return self.board

class Knight(Pieces):  
    def __init__(self, init_position, colour='White'):
        #super().__init__()
        self.position = init_position
        self.colour = colour
    

    def possible_moves(self, steps, start, end):
        """
        Defines possible moves available to a piece
        """
        polist(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        pass 



        

class Rook(Pieces):  
    def __init__(self, init_position):
        self.position = init_position
    
    def return_possible_positions(self):
        return self.position

class Queen(Pieces):  
    def __init__(self, init_position):
        self.position = init_position
        
    def possible_moves(self, steps, start, end):
        """
        Defines possible moves available to a piece
        """
        pass
        
class Bishop(Pieces):  
    def __init__(self, init_position):
        self.position = init_position
        
        pass
    
    def possible_positions(self, init_position):
        pass

def simplifiedChessEngine(whites, blacks, m):
    board = Board(whites, blacks, squares=4)
    for _ in whites:


        
        

