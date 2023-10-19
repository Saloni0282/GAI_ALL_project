# import os

# # Function to create a new game board of a specified size
# def create_board(board_size):
#     return [[" " for _ in range(board_size)] for _ in range(board_size)]

# # Function to display the game board
# def display_board(board):
#     for row in board:
#         print(" | ".join(row))
#         print("-" * (4 * len(row) - 1))

# # Function to check if a player has won
# def check_win(board, player):
#     size = len(board)
    
#     # Check rows, columns, and diagonals
#     for i in range(size):
#         if all(board[i][j] == player for j in range(size)) or \
#            all(board[j][i] == player for j in range(size)):
#             return True
#     if all(board[i][i] == player for i in range(size)) or \
#        all(board[i][size - 1 - i] == player for i in range(size)):
#         return True
#     return False

# # Function to check for a tie
# def check_tie(board):
#     return all(board[i][j] != " " for i in range(len(board)) for j in range(len(board)))

# # Function to take player input and make a move
# def make_move(board, player, player_moves):
#     while True:
#         display_board(board)
#         print(f"Player {player}'s turn")
#         row = input(f"Enter the row (0 to {len(board) - 1}): ")
#         col = input(f"Enter the column (0 to {len(board) - 1}): ")
        
#         if row.isdigit() and col.isdigit():
#             row = int(row)
#             col = int(col)
            
#             if 0 <= row < len(board) and 0 <= col < len(board):
#                 if board[row][col] == " ":
#                     board[row][col] = player
#                     player_moves.append((row, col))  # Store the move for potential undo
#                     return row, col  # Return the row and col values
#                 else:
#                     print("That cell is already occupied. Try again.")
#             else:
#                 print(f"Invalid input. Row and column should be between 0 and {len(board) - 1}.")

#         else:
#             print("Invalid input. Please enter integers for row and column.")

# # Function to choose the board size
# def choose_board_size():
#     while True:
#         size = input("Choose the board size (e.g., '3' for 3x3, '4' for 4x4): ")
#         if size.isdigit() and int(size) >= 3:
#             return int(size)
#         else:
#             print("Invalid input. Please enter a number greater than or equal to 3.")

# # Function to update player scores
# def update_scores(player, scores):
#     if player in scores:
#         scores[player] += 1
#     else:
#         scores[player] = 1

# # Function to display player scores
# def display_scores(scores):
#     print("Player Scores:")
#     for player, score in scores.items():
#         print(f"Player {player}: {score}")

# # Function to undo the last move
# def undo_move(board, player_moves):
#     if player_moves:
#         last_move = player_moves.pop()
#         row, col = last_move
#         board[row][col] = " "

# # Function to display the game history
# def display_history(history):
#     print("Game History:")
#     for move in history:
#         player, row, col = move
#         print(f"Player {player}: Row {row}, Column {col}")

# # Main game loop
# scores = {}  # Initialize player scores
# while True:
#     os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
#     print("Welcome to Advanced Tic-Tac-Toe!")
    
#     board_size = choose_board_size()
#     board = create_board(board_size)
#     current_player = "X"
#     player_x_moves = []  # List to store player X's moves for undo
#     player_o_moves = []  # List to store player O's moves for undo
#     game_history = []  # List to store game history
    
#     # Game loop for a single match
#     while True:
#         if current_player == "X":
#             row, col = make_move(board, current_player, player_x_moves)  # Get row and col from the make_move function
#         else:
#             row, col = make_move(board, current_player, player_o_moves)  # Get row and col from the make_move function
        
#         game_history.append((current_player, row, col))  # Store the move in game history
        
#         if check_win(board, current_player):
#             display_board(board)
#             print(f"Player {current_player} wins!")
#             update_scores(current_player, scores)
#             display_scores(scores)
#             break
#         elif check_tie(board):
#             display_board(board)
#             print("It's a tie!")
#             display_scores(scores)
#             break
        
#         # Ask if the current player wants to undo a move
#         undo_option = input(f"Player {current_player}, undo the last move? (yes/no): ")
#         if undo_option.lower() == "yes":
#             if current_player == "X":
#                 undo_move(board, player_x_moves)  # Undo the last move for player X
#             else:
#                 undo_move(board, player_o_moves)  # Undo the last move for player O
#             game_history.pop()  # Remove the undone move from game history
#         else:
#             current_player = "O" if current_player == "X" else "X"  # Switch to the other player
    
#     # Ask if players want to review game history or start a new game
#     review_option = input("Review game history? (yes/no): ")
#     if review_option.lower() == "yes":
#         display_history(game_history)
    
#     new_game = input("Start a new game? (yes/no): ")
#     if new_game.lower() != "yes":
#         break

# print("Thanks for playing!")

import os
import json

# Function to create a new game board of a specified size
def create_board(board_size):
    return [[" " for _ in range(board_size)] for _ in range(board_size)]

# Function to display the game board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * (4 * len(row) - 1))

# Function to check if a player has won
def check_win(board, player):
    size = len(board)
    
    # Check rows, columns, and diagonals
    for i in range(size):
        if all(board[i][j] == player for j in range(size)) or \
           all(board[j][i] == player for j in range(size)):
            return True
    if all(board[i][i] == player for i in range(size)) or \
       all(board[i][size - 1 - i] == player for i in range(size)):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all(board[i][j] != " " for i in range(len(board)) for j in range(len(board)))

# Function to take player input and make a move
def make_move(board, player, player_moves):
    while True:
        display_board(board)
        print(f"Player {player}'s turn")
        row = input(f"Enter the row (0 to {len(board) - 1}): ")
        col = input(f"Enter the column (0 to {len(board) - 1}): ")
        
        if row.isdigit() and col.isdigit():
            row = int(row)
            col = int(col)
            
            if 0 <= row < len(board) and 0 <= col < len(board):
                if board[row][col] == " ":
                    board[row][col] = player
                    player_moves.append((row, col))  # Store the move for potential undo
                    return row, col  # Return the row and col values
                else:
                    print("That cell is already occupied. Try again.")
            else:
                print(f"Invalid input. Row and column should be between 0 and {len(board) - 1}.")

        else:
            print("Invalid input. Please enter integers for row and column.")

# Function to choose the board size
def choose_board_size():
    while True:
        size = input("Choose the board size (e.g., '3' for 3x3, '4' for 4x4): ")
        if size.isdigit() and int(size) >= 3:
            return int(size)
        else:
            print("Invalid input. Please enter a number greater than or equal to 3.")

# Function to update player scores
def update_scores(player, scores):
    if player in scores:
        scores[player] += 1
    else:
        scores[player] = 1

# Function to display player scores
def display_scores(scores):
    print("Player Scores:")
    for player, score in scores.items():
        print(f"Player {player}: {score}")

# Function to undo the last move
def undo_move(board, player_moves):
    if player_moves:
        last_move = player_moves.pop()
        row, col = last_move
        board[row][col] = " "

# Function to display the game history
def display_history(history):
    print("Game History:")
    for move in history:
        player, row, col = move
        print(f"Player {player}: Row {row}, Column {col}")

def save_game_to_json(board, current_player, player_x_moves, player_o_moves, game_history):
    game_data = {
        "board": board,
        "current_player": current_player,
        "player_x_moves": player_x_moves,
        "player_o_moves": player_o_moves,
        "game_history": game_history
    }
    with open("tictactoe_save.json", "w") as save_file:
        json.dump(game_data, save_file)
        
# Function to load a saved game from a JSON file
def load_game_from_json():
    if os.path.exists("tictactoe_save.json") and os.path.getsize("tictactoe_save.json") > 0:
        try:
            with open("tictactoe_save.json", "r") as save_file:
                game_data = json.load(save_file)
                board = game_data["board"]
                current_player = game_data["current_player"]
                player_x_moves = game_data["player_x_moves"]
                player_o_moves = game_data["player_o_moves"]
                game_history = game_data["game_history"]
                return board, current_player, player_x_moves, player_o_moves, game_history
        except Exception as e:
            print(f"An error occurred while loading the game: {str(e)}")
    return None

# Main game loop
scores = {}  # Initialize player scores
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
    print("Welcome to Advanced Tic-Tac-Toe!")
    
    board_size = choose_board_size()
    board = create_board(board_size)
    current_player = "X"
    player_x_moves = []  # List to store player X's moves for undo
    player_o_moves = []  # List to store player O's moves for undo
    game_history = []  # List to store game history
    
    # Check if the game should be loaded
    load_option = input("Do you want to load a saved game? (yes/no): ")
    if load_option.lower() == "yes":
        loaded_game = load_game_from_json()
        if loaded_game is not None:
            board, current_player, player_x_moves, player_o_moves, game_history = loaded_game
        else:
            print("No saved game available.")
            continue  # Start a new game if no saved game is available
    
    # Game loop for a single match
    while True:
        if current_player == "X":
            row, col = make_move(board, current_player, player_x_moves)  # Get row and col from the make_move function
        else:
            row, col = make_move(board, current_player, player_o_moves)  # Get row and col from the make_move function
        
        game_history.append((current_player, row, col))  # Store the move in game history
        
        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            update_scores(current_player, scores)
            display_scores(scores)
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            display_scores(scores)
            break
        
        # Ask if the current player wants to undo a move
        undo_option = input(f"Player {current_player}, undo the last move? (yes/no): ")
        if undo_option.lower() == "yes":
            if current_player == "X":
                undo_move(board, player_x_moves)  # Undo the last move for player X
            else:
                undo_move(board, player_o_moves)  # Undo the last move for player O
            game_history.pop()  # Remove the undone move from game history
        else:
            current_player = "O" if current_player == "X" else "X"  # Switch to the other player
    
    # Ask if players want to review game history, save the game, or start a new game
    review_option = input("Review game history, save the game, or start a new game? (review/save/no): ")
    if review_option.lower() == "review":
        display_history(game_history)
    elif review_option.lower() == "save":
        save_game_to_json(board, current_player, player_x_moves, player_o_moves, game_history)
    
    new_game = input("Start a new game? (yes/no): ")
    if new_game.lower() != "yes":
        break

print("Thanks for playing!")
