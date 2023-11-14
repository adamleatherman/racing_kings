# Author: Adam Leatherman
# GitHub username: adamleatherman
# Date: 8/12/2023
# Description: Abstract variant of Racing Kings, a chess variant where players must move their kings to rank 8 but
#              cannot check enemy king.


class ChessVar:
    def __init__(self):
        self._board = {
            "a8": "_", "b8": "_", "c8": "_", "d8": "_", "e8": "_", "f8": "_", "g8": "_", "h8": "_",
            "a7": "_", "b7": "_", "c7": "_", "d7": "_", "e7": "_", "f7": "_", "g7": "_", "h7": "_",
            "a6": "_", "b6": "_", "c6": "_", "d6": "_", "e6": "_", "f6": "_", "g6": "_", "h6": "_",
            "a5": "_", "b5": "_", "c5": "_", "d5": "_", "e5": "_", "f5": "_", "g5": "_", "h5": "_",
            "a4": "_", "b4": "_", "c4": "_", "d4": "_", "e4": "_", "f4": "_", "g4": "_", "h4": "_",
            "a3": "_", "b3": "_", "c3": "_", "d3": "_", "e3": "_", "f3": "_", "g3": "_", "h3": "_",
            "a2": "R", "b2": "B", "c2": "N", "d2": "_", "e2": "_", "f2": "n", "g2": "b", "h2": "r",
            "a1": "K", "b1": "B", "c1": "N", "d1": "_", "e1": "_", "f1": "n", "g1": "b", "h1": "k"
        }
        self._game_state = "UNFINISHED"
        self._turn = "WHITE"
        self._unicode = {
            "B": "♗",
            "b": "♝",
            "R": "♖",
            "r": "♜",
            "N": "♘",
            "n": "♞",
            "K": "♔",
            "k": "♚",
            "_": " _ "
        }
        
    def print_board(self):
        """Prints board state"""
        print()
        for rank in range(8, 0, -1):
            print(f"{rank} ", end="|")
            for file in "abcdefgh":
                square = file + str(rank)
                print(self._unicode[self._board[square]], end="|")

            print()
        print("   a  b  c d e  f  g  h")
        print()
        
    def pre_checks(self, move_from, move_to):
        """Returns False if valid move conditions are not met"""
        # If game is over
        if self._game_state != "UNFINISHED":
            print("Game is already over!")
            return False
        
        # If starting or ending square not a valid square
        elif move_from not in self._board or move_to not in self._board:
            print("Invalid move. One or both of the squares are not on board.")
            return False
        
        # If white is trying to move a black piece
        elif self._turn == "WHITE" and self._board[move_from].islower():
            print("Invalid move. You must move a white piece.")
            return False
        
        # If black is trying to move a white piece
        elif self._turn == "BLACK" and self._board[move_from].isupper():
            print("Invalid move. You must move a black piece.")
            return False
        
        # If no piece to be moved
        elif self._board[move_from] == "_":
            print("Invalid move. No piece to be moved.")
            return False
        
        # If starting and ending squares are the same
        elif move_from == move_to:
            print("Invalid move. Starting and ending squares are the same.")
            return False
        
        return True
    
    def get_bishop_moves(self, square, board=None, turn=None):
        """Returns a list of squares that a bishop can move to """
        valid_moves = []
        files = "abcdefgh"
        ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        starting_file = square[0]
        starting_rank = int(square[1])
        starting_file_index = files.index(starting_file)
        starting_rank_index = ranks.index(starting_rank)
        
        # Initialize default parameters if not passed
        if board is None:
            board = self._board
        if turn is None:
            turn = self._turn
        
        # Get moves upper-right
        temp_rank_index = starting_rank_index
        for i in range(starting_file_index + 1, len(files)):
            temp_rank_index += 1
            if temp_rank_index >= len(ranks):
                break
            current_square = files[i] + str(ranks[temp_rank_index])            # Adding all blank squares to move list
            if board[current_square] == "_":

                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves upper-left
        temp_rank_index = starting_rank_index
        for i in range(starting_file_index - 1, -1, -1):
            temp_rank_index += 1
            if temp_rank_index >= len(ranks):
                break
            current_square = files[i] + str(ranks[temp_rank_index])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves lower-left
        temp_rank_index = starting_rank_index
        for i in range(starting_file_index - 1, -1, -1):
            temp_rank_index -= 1
            if temp_rank_index < 0:
                break
            current_square = files[i] + str(ranks[temp_rank_index])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves lower-right
        temp_rank_index = starting_rank_index
        for i in range(starting_file_index + 1, len(files)):
            temp_rank_index -= 1
            if temp_rank_index < 0:
                break
            current_square = files[i] + str(ranks[temp_rank_index])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        return valid_moves
    
    def get_rook_moves(self, square, board=None, turn=None):
        """Returns a list of squares that a rook can move to"""
        valid_moves = []
        files = "abcdefgh"
        ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        starting_file = square[0]
        starting_rank = int(square[1])
        starting_file_index = files.index(starting_file)
        starting_rank_index = ranks.index(starting_rank)
        
        # Initialize default parameters if not passed
        if board is None:
            board = self._board
        if turn is None:
            turn = self._turn
        
        # Get moves upper
        for i in range(starting_rank_index + 1, len(ranks)):
            current_square = starting_file + str(ranks[i])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves lower
        for i in range(starting_rank_index - 1, -1, -1):
            current_square = starting_file + str(ranks[i])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves right
        for i in range(starting_file_index + 1, len(files)):
            current_square = files[i] + str(ranks[starting_rank_index])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        # Get moves left
        for i in range(starting_file_index - 1, -1, -1):
            current_square = files[i] + str(ranks[starting_rank_index])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
                break
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
                break
            # Own piece is in the way, stop loop
            else:
                break
        
        return valid_moves
    
    def get_knight_moves(self, square, board=None, turn=None):
        """Returns a list of squares that a knight can move to"""
        valid_moves = []
        files = "abcdefgh"
        ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        starting_file = square[0]
        starting_rank = int(square[1])
        starting_file_index = files.index(starting_file)
        starting_rank_index = ranks.index(starting_rank)
        
        # Initialize default parameters if not passed
        if board is None:
            board = self._board
        if turn is None:
            turn = self._turn
        
        # 2 ranks up, 1 file right
        if starting_rank_index + 2 < len(ranks) and starting_file_index + 1 < len(files):
            current_square = files[starting_file_index + 1] + str(ranks[starting_rank_index + 2])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 2 ranks up, 1 file left
        if starting_rank_index + 2 < len(ranks) and starting_file_index - 1 > -1:
            current_square = files[starting_file_index - 1] + str(ranks[starting_rank_index + 2])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 1 rank up, 2 files right
        if starting_rank_index + 1 < len(ranks) and starting_file_index + 2 < len(files):
            current_square = files[starting_file_index + 2] + str(ranks[starting_rank_index + 1])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 1 rank up, 2 files left
        if starting_rank_index + 1 < len(ranks) and starting_file_index - 2 > -1:
            current_square = files[starting_file_index - 2] + str(ranks[starting_rank_index + 1])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 2 ranks down, 1 file right
        if starting_rank_index - 2 > -1 and starting_file_index + 1 < len(files):
            current_square = files[starting_file_index + 1] + str(ranks[starting_rank_index - 2])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 2 ranks down, 1 file left
        if starting_rank_index - 2 > -1 and starting_file_index - 1 > -1:
            current_square = files[starting_file_index - 1] + str(ranks[starting_rank_index - 2])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 1 rank down, 2 files right
        if starting_rank_index - 1 > -1 and starting_file_index + 2 < len(files):
            current_square = files[starting_file_index + 2] + str(ranks[starting_rank_index - 1])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # 1 rank down, 2 files left
        if starting_rank_index - 1 > -1 and starting_file_index - 2 > -1:
            current_square = files[starting_file_index - 2] + str(ranks[starting_rank_index - 1])
            # Adding blank square to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        return valid_moves
    
    def get_king_moves(self, square, board=None, turn=None):
        """Returns a list of squares that a king can move to"""
        valid_moves = []
        files = "abcdefgh"
        ranks = [1, 2, 3, 4, 5, 6, 7, 8]
        starting_file = square[0]
        starting_rank = int(square[1])
        starting_file_index = files.index(starting_file)
        starting_rank_index = ranks.index(starting_rank)
        
        # Initialize default parameters if not passed
        if board is None:
            board = self._board
        if turn is None:
            turn = self._turn
        
        # Get moves upper
        if starting_rank_index + 1 < len(ranks):
            current_square = starting_file + str(ranks[starting_rank_index + 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves lower
        if starting_rank_index - 1 > -1:
            current_square = starting_file + str(ranks[starting_rank_index - 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves right
        if starting_file_index + 1 < len(files):
            current_square = files[starting_file_index + 1] + str(starting_rank)
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves left
        if starting_file_index - 1 > -1:
            current_square = files[starting_file_index - 1] + str(starting_rank)
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves upper-right
        if starting_rank_index + 1 < len(ranks) and starting_file_index + 1 < len(files):
            current_square = files[starting_file_index + 1] + str(ranks[starting_rank_index + 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves upper-left
        if starting_rank_index + 1 < len(ranks) and starting_file_index - 1 > -1:
            current_square = files[starting_file_index - 1] + str(ranks[starting_rank_index + 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves lower-right
        if starting_rank_index - 1 > -1 and starting_file_index + 1 < len(files):
            current_square = files[starting_file_index + 1] + str(ranks[starting_rank_index - 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        # Get moves lower-left
        if starting_rank_index - 1 > -1 and starting_file_index - 1 > -1:
            current_square = files[starting_file_index - 1] + str(ranks[starting_rank_index - 1])
            # Adding all blank squares to move list
            if board[current_square] == "_":
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "WHITE" and board[current_square].islower():
                valid_moves.append(current_square)
            # Adding final square if opponent piece encountered
            elif turn == "BLACK" and board[current_square].isupper():
                valid_moves.append(current_square)
        
        return valid_moves
    
    def both_kings_safe(self, move_from, move_to):
        """Simulates a move to determine both kings' safety"""
        # Save current board in variable and find location of kings
        board_placeholder = self._board.copy()
        turn_placeholder = self._turn
        move_from_lower = move_from.lower()
        move_to_lower = move_to.lower()
        piece = self._board[move_from_lower]
        
        # Simulate move
        board_placeholder[move_to_lower] = board_placeholder[move_from_lower]
        board_placeholder[move_from_lower] = "_"
        if turn_placeholder == "WHITE":
            turn_placeholder = "BLACK"
        else:
            turn_placeholder = "WHITE"
        
        # Find location of kings
        white_king_location = None
        black_king_location = None
        for square in board_placeholder:
            if board_placeholder[square] == "K":
                white_king_location = square
                break
        for square in board_placeholder:
            if board_placeholder[square] == "k":
                black_king_location = square
                break
        
        # If either king is no longer on the board, invalid move. Can't capture kings!
        # Shouldn't ever get to this block if check controlled properly.
        if white_king_location is None or black_king_location is None:
            return False
        
        # If move puts another king in check, including discovered checks, invalid move
        if piece == "B":
            new_paths = self.get_bishop_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "k":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "R":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "B":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "b":
            new_paths = self.get_bishop_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "K":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "r":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "b":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "R":
            new_paths = self.get_rook_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "k":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "R":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "B":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "r":
            new_paths = self.get_rook_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "K":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "r":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "b":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "N":
            new_paths = self.get_knight_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "k":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "R":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "B":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "n":
            new_paths = self.get_knight_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "K":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "r":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "b":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "K":
            new_paths = self.get_king_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "k":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "R":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(black_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "B":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        elif piece == "k":
            new_paths = self.get_king_moves(move_to_lower, board_placeholder)
            for square in new_paths:
                if board_placeholder[square] == "K":
                    print("Cannot place enemy in check!")
                    return False
            discovered_rook_checks = self.get_rook_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_rook_checks:
                if board_placeholder[square] == "r":
                    print("Cannot place enemy in check! Discovered check by rook.")
                    return False
            discovered_bishop_checks = self.get_bishop_moves(white_king_location, board_placeholder, turn_placeholder)
            for square in discovered_bishop_checks:
                if board_placeholder[square] == "b":
                    print("Cannot place enemy in check! Discovered check by bishop.")
                    return False
        
        # White moves; If move exposes own king to check, invalid move
        if turn_placeholder == "BLACK":  # White just moved
            # Check for rooks
            rook_threats = self.get_rook_moves(white_king_location, board_placeholder)
            for square in rook_threats:
                if board_placeholder[square] == "r":
                    print("Move exposes king to enemy rook!")
                    return False
            
            # Check for knights
            knight_threats = self.get_knight_moves(white_king_location, board_placeholder)
            for square in knight_threats:
                if board_placeholder[square] == "n":
                    print("Move exposes king to enemy knight!")
                    return False
            
            # Check for bishops
            bishop_threats = self.get_bishop_moves(white_king_location, board_placeholder)
            for square in bishop_threats:
                if board_placeholder[square] == "b":
                    print("Move exposes king to enemy bishop!")
                    return False
        
        # Black moves; If move exposes own king to check, invalid move
        else:  # Black just moved
            # Check for rooks
            rook_threats = self.get_rook_moves(black_king_location, board_placeholder)
            for square in rook_threats:
                if board_placeholder[square] == "R":
                    print("Move exposes king to enemy rook!")
                    return False
            
            # Check for knights
            knight_threats = self.get_knight_moves(black_king_location, board_placeholder)
            for square in knight_threats:
                if board_placeholder[square] == "N":
                    print("Move exposes king to enemy knight!")
                    return False
            
            # Check for bishops
            bishop_threats = self.get_bishop_moves(black_king_location, board_placeholder)
            for square in bishop_threats:
                if board_placeholder[square] == "B":
                    print("Move exposes king to enemy bishop!")
                    return False
        
        return True
    
    def get_game_state(self):
        """Returns game state"""
        return self._game_state
    
    def get_turn(self):
        """Returns current player's turn"""
        return self._turn
    
    def is_game_over(self):
        """Checks game over conditions"""
        white_king_on_eight = False
        black_king_on_eight = False
        for square in self._board:
            if square[1] == "8":
                piece = self._board[square]
                if piece == "K":
                    white_king_on_eight = True
                    break
        for square in self._board:
            if square[1] == "8":
                piece = self._board[square]
                if piece == "k":
                    black_king_on_eight = True
                    break
        
        if white_king_on_eight and not black_king_on_eight and self._turn == "WHITE":
            self._game_state = "WHITE_WON"
        
        elif black_king_on_eight and not white_king_on_eight and self._turn == "BLACK":
            self._game_state = "BLACK_WON"
        
        elif white_king_on_eight and black_king_on_eight:
            self._game_state = "TIE"
        
        elif white_king_on_eight and not black_king_on_eight and self._turn == "BLACK":
            print("One move remaining!")
        
        elif black_king_on_eight and not white_king_on_eight and self._turn == "WHITE":
            print("One move remaining!")
    
    def make_move(self, move_from, move_to):
        """Moves a piece from a square to a destination"""
        move_from_lower = move_from.lower()
        move_to_lower = move_to.lower()
        
        # Perform pre-checks
        if not self.pre_checks(move_from_lower, move_to_lower):
            return False
        
        piece = self._board[move_from_lower]
        
        # Valid move check
        if piece == "B" or piece == "b":
            valid_moves = self.get_bishop_moves(move_from_lower)
            if move_to_lower not in valid_moves:
                print("A bishop can't make this move!")
                return False
        
        elif piece == "R" or piece == "r":
            valid_moves = self.get_rook_moves(move_from_lower)
            if move_to_lower not in valid_moves:
                print("A rook can't make this move!")
                return False
        
        elif piece == "N" or piece == "n":
            valid_moves = self.get_knight_moves(move_from_lower)
            if move_to_lower not in valid_moves:
                print("A knight can't make this move!")
                return False
        
        elif piece == "K" or piece == "k":
            valid_moves = self.get_king_moves(move_from_lower)
            if move_to_lower not in valid_moves:
                print("A king can't make this move!")
                return False
        
        # Check for kings' safety after simulating move
        if not self.both_kings_safe(move_from_lower, move_to_lower):
            return False
        
        # Make the move once validity determined
        self._board[move_to_lower] = piece
        self._board[move_from_lower] = "_"
        
        # Update turn
        if self._turn == "WHITE":
            self._turn = "BLACK"
        else:
            self._turn = "WHITE"
            
        # Check for game over conditions and set game state accordingly
        self.is_game_over()
        
        if self._game_state == "UNFINISHED":
            print(self._turn + " to move.")
            return True
        
        # If game is over
        elif self._game_state == "WHITE_WON":
            print("Game over! White wins!")
            return False
        
        elif self._game_state == "BLACK_WON":
            print("Game over! Black wins!")
            return False
        
        elif self._game_state == "TIE":
            print("Game over! The game is a tie!")
            return False
