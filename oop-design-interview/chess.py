from enum import Enum
from abc import ABC, abstractmethod

class Color(Enum):
    WHITE = 0
    BLACK = 1

class Square:
    def __init__(self, color):
        self.color = color
        self.piece = None

    def get_piece(self):
        return self.piece
    
    def get_color(self):
        return self.color
    
    def set_piece(self, piece):
        self.piece = piece

class Piece(ABC):
    def __init__(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
    @staticmethod
    def is_within_grid(end_row, end_col):
        return 0 <= end_row <= 7 and 0 <= end_col <= 7
    
    @abstractmethod
    def is_valid_move(self, start_row, start_col, end_row, end_col):
        pass
    
    @abstractmethod
    def get_symbol(self):
        pass
    
class Pawn(Piece):
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not self.is_within_grid(end_row, end_col):
            return False
        
        row_movement = end_row - start_row
        col_movement = end_col - start_col
        direction = -1 if self.get_color() == Color.WHITE else 1

        is_kill_move = abs(col_movement) == 1 and abs(row_movement) == 1 and board[end_row][end_col].get_piece() is not None and board[start_row][start_col].get_piece().get_color() != board[end_row][end_col].get_piece().get_color()

        # Check if the pawn is moving diagonally
        if col_movement != 0 and not is_kill_move:
            return False
        
        # Check if pawn could kill a piece
        if is_kill_move:
            return True
        
        # Check if the pawn is moving forward
        if row_movement == direction and board[end_row][end_col].get_piece() is None:
            return True
        
        # Check if the pawn is moving two steps forward on its first move
        if (self.is_first_move(start_row) and row_movement == (2 * direction) and 
            board[start_row + direction][start_col].get_piece() is None and
            board[end_row][end_col].get_piece() is None):
            return True
        
        return False
    
    def get_symbol(self):
      return 'P' if self.get_color() == Color.WHITE else 'p'
    
    def is_first_move(self, start_row):
        return (self.get_color() == Color.WHITE and start_row == 6) or \
               (self.get_color() == Color.BLACK and start_row == 1)
    
class Knight(Piece):
    
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not self.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        # Check if the knight is moving in an L shape
        if row_movement == 2 and col_movement == 1 or \
           row_movement == 1 and col_movement == 2:
            # Check if the knight is not moving to a square with the same color piece
            if board[end_row][end_col].get_piece() is not None and \
               board[end_row][end_col].get_piece().get_color() == self.get_color():
                return False
            
            return True
        
        return False
    
    def get_symbol(self):
        return "N" if self.get_color() == Color.WHITE else "n"
    
class MovementUtil:
    
    @staticmethod
    def is_valid_straight_move(start_row, start_col, end_row, end_col, color, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement != 0 and col_movement != 0 or (row_movement == 0 and col_movement == 0):
            # The piece is not moving in a straight line
            return False
        else:
            # increment is 1 if direction is positive, -1 otherwise
            row_increment = 1 if end_row > start_row else -1
            col_increment = 1 if end_col > start_col else -1

            # Check if there are any pieces in the path
            if row_movement == 0:
                # Moving horizontally
                y = start_col + col_increment
                while y != end_col:
                    if board[start_row][y].get_piece() is not None:
                        return False
                    y += col_increment

            else:
                # Moving vertically
                x = start_row + row_increment

                while x != end_row:
                    if board[x][start_col].get_piece() is not None:
                        return False
                    
                    x += row_increment

            # Check if the piece is moving to a square with the same color piece
            if board[end_row][end_col].get_piece() is not None and \
               board[end_row][end_col].get_piece().get_color() == color:
                return False
            
            # The move is valid
            return True
      
    @staticmethod
    def is_valid_diagonal_move(start_row, start_col, end_row, end_col, color, board):
      if not Piece.is_within_grid(end_row, end_col):
          # The move is outside the board
          return False
      
      row_movement = abs(end_row - start_row)
      col_movement = abs(end_col - start_col)

      if row_movement == col_movement:
          # The piece is moving diagonally
          row_increment = 1 if end_row > start_row else -1
          col_increment = 1 if end_col > start_col else -1

          x, y = start_row + row_increment, start_col + col_increment

          while x != end_row and y != end_col:
              if board[x][y].get_piece() is not None:
                  # There is a piece in the path
                  return False
              
              x += row_increment
              y += col_increment

          if board[end_row][end_col].get_piece() is not None and \
             board[end_row][end_col].get_piece().get_color() == color:
              # The piece is moving to a square with the same color piece
              return False
          
          # The move is valid
          return True
      else:
          # The piece is not moving diagonally
          return False
      
class Rook(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return MovementUtil.is_valid_straight_move(start_row, start_col, end_row, end_col, self.get_color(), board)
    
    def get_symbol(self):
        return "R" if self.get_color() == Color.WHITE else "r"
    
class Bishop(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return MovementUtil.is_valid_diagonal_move(start_row, start_col, end_row, end_col, self.get_color(), board)
    
    def get_symbol(self):
        return "B" if self.get_color() == Color.WHITE else "b"
    
class King(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        if not Piece.is_within_grid(end_row, end_col):
            return False
        
        row_movement = abs(end_row - start_row)
        col_movement = abs(end_col - start_col)

        if row_movement > 1 or col_movement > 1:
            # The king is moving more than one square
            return False

        if board[end_row][end_col].get_piece() is not None and \
           board[end_row][end_col].get_piece().get_color() == self.get_color():
            # The king is moving to a square with the same color piece
            return False
        
        # The move is valid
        return True
    
    def get_symbol(self):
        return "K" if self.get_color() == Color.WHITE else "k"
    
class Queen(Piece):
    def is_valid_move(self, start_row, start_col, end_row, end_col, board):
        return \
                MovementUtil.is_valid_straight_move(start_row, start_col, end_row, end_col, self.      get_color(), board) or \
                MovementUtil.is_valid_diagonal_move(start_row, start_col, end_row, end_col, self.get_color(), board)
    
    def get_symbol(self):
        return "Q" if self.get_color() == Color.WHITE else "q"
    
class Player:
    def __init__(self, color):
        self.color = color
    
    def get_color(self):
        return self.color
    
class ChessBoard:
    
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board_and_pieces()

    def initialize_board_and_pieces(self):
        for i in range(8):
            for j in range(8):
                square_color = Color.BLACK if (i + j) % 2 == 0 else Color.WHITE
                self.board[i][j] = Square(square_color)


        self.initialize_black_pieces()
        self.initialize_white_pieces()

    def initialize_black_pieces(self):
        for i in range(8):
            self.board[1][i].set_piece(Pawn(Color.BLACK))

        self.board[0][0].set_piece(Rook(Color.BLACK))
        self.board[0][7].set_piece(Rook(Color.BLACK))
        self.board[0][1].set_piece(Knight(Color.BLACK))
        self.board[0][6].set_piece(Knight(Color.BLACK))
        self.board[0][2].set_piece(Bishop(Color.BLACK))
        self.board[0][5].set_piece(Bishop(Color.BLACK))
        self.board[0][3].set_piece(Queen(Color.BLACK))
        self.board[0][4].set_piece(King(Color.BLACK))

    def initialize_white_pieces(self):
        for i in range(8):
            self.board[6][i].set_piece(Pawn(Color.WHITE))

        self.board[7][0].set_piece(Rook(Color.WHITE))
        self.board[7][7].set_piece(Rook(Color.WHITE))
        self.board[7][1].set_piece(Knight(Color.WHITE))
        self.board[7][6].set_piece(Knight(Color.WHITE))
        self.board[7][2].set_piece(Bishop(Color.WHITE))
        self.board[7][5].set_piece(Bishop(Color.WHITE))
        self.board[7][3].set_piece(Queen(Color.WHITE))
        self.board[7][4].set_piece(King(Color.WHITE))

    def move_piece(self, current_player):
        while True:
            start_row = int(input("Enter starting row: "))
            start_col = int(input("Enter starting column: "))
            end_row = int(input("Enter destination row: "))
            end_col = int(input("Enter destination column: "))

            if not Piece.is_within_grid(end_row, end_col):
                continue
            
            piece_to_move = self.board[start_row][start_col].get_piece()

            if not piece_to_move:
                print("No piece at the starting position. Please try again.")
                continue
            
            if piece_to_move.get_color() != current_player.get_color():
                print("You cannot move the opponent's piece. Please try again.")
                continue
            
            if piece_to_move.is_valid_move(start_row, start_col, end_row, end_col, self.board):
                destination_piece = self.board[end_row][end_col].get_piece()
                if destination_piece and destination_piece.color != piece_to_move:
                    # Capture the opponent's piece
                    self.board[end_row][end_col].set_piece(None)

                self.board[end_row][end_col].set_piece(piece_to_move)
                self.board[start_row][start_col].set_piece(None)
                print(f"{piece_to_move.get_symbol()} moved from ({start_row}, {start_col}) to ({end_row}, {end_col})")
                return True
            else:
                print(f"Invalid move for the {piece_to_move.get_symbol()}. Please try again.")

    def display_board(self):
      print("  0 1 2 3 4 5 6 7")
      print("  ---------------")
      for i in range(8):
          print(i, end="|")
          for j in range(8):
              peice = self.board[i][j].get_piece()
              print(peice.get_symbol() + " " if peice else ". ", end="")
          print() 

class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.white_player = Player(Color.WHITE)
        self.black_player = Player(Color.BLACK)
        self.current_player = self.white_player

    def start_game(self):
        print("Welcome to Chess! UPPERCASE denotes white pieces and lowercase denotes black pieces.")
        self.board.display_board()

        current_player = self.white_player

        while True:
            print("Current turn:" + str(current_player.get_color()))

            move_successful = self.board.move_piece(self.current_player)
            if move_successful:
                self.board.display_board()
                self.current_player = self.black_player if self.current_player == self.white_player else self.white_player
            else: 
                print("Invalid move. Please try again.")

if __name__ == '__main__':
    game = ChessGame()
    game.start_game()