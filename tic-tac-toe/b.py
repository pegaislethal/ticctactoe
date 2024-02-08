# import random
# import os.path
# import json
#
# random.seed()
# # Name- Rohit Ghimire
# # Student id - 2408291
#
#
# def draw_board(board):
#     """
#     I have used this function to print the board using loop
#     :param board:
#     :return:
#     """
#     # looping to print the board
#     for i in range(0, 3):
#         print(" ----------------")
#         for j in range(0, 3):
#             print("|", board[i][j], end=" | ")
#         print()
#     print(" ----------------")
#
#
# def welcome(board):
#     # prints the welcome message
#     # display the board by calling draw_board(board)
#     print('Welcome to the "Unbeatable Noughts and Crosses" game.')
#     print("The board layout is below:")
#     draw_board(board)
#     print("When prompted, enter the number corresponding to the square you want.")
#
#
# def initialise_board(board):
#     """
#     It will empty the board which was print in the draw_board function
#     :param board:
#     :return:
#     """
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             board[i][j] = ' '
#     return board
#
#
# def get_player_move(board):
#     """
#     This function ask the user row and column as input
#     :param board:
#     :return:
#     """
#     while True:
#         try:
#             row = int(input("Enter the row (0, 1, or 2): "))
#             col = int(input("Enter the column (0, 1, or 2): "))
#             if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
#                 return row, col
#             print("Invalid move. Try again.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#
#
# def choose_computer_move(board):
#     """
#     This function randomly generates the number
#     :param board:
#     :return:
#     """
#     while True:
#         row = random.randint(0, 2)
#         col = random.randint(0, 2)
#         if board[row][col] == " ":
#             break
#     return row, col
#
#
# def check_for_win(board, mark):
#     for i in range(3):
#         if all(board[i][j] == mark for j in range(3)) or all(board[j][i] == mark for j in range(3)):
#             return True
#     if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
#         return True
#     return False
#
#
# def check_for_draw(board):
#     # develop cope to check if all cells are occupied
#     # return True if it is, False otherwise
#     if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
#         return True
#     return False
#
#
# def play_game(board):
#     """
#     This function calls the tow function to keep the input in one space and call another function
#     to display the empty board
#     Then we have loop which ask the user to input numbers
#     :param board:
#     :return: 1 or 0 or -1
#     """
#     initialise_board(board)
#     draw_board(board)
#
#     while True:
#         row, column = get_player_move(board)
#         board[row][column] = 'X'
#         draw_board(board)
#
#         if check_for_win(board, "X"):
#             print("Booyah!! you win")
#             return 1
#         if check_for_draw(board):
#             print("Tie game,GG!")
#             return 0
#
#         row, col = choose_computer_move(board)
#         board[row][col] = 'O'
#         draw_board(board)
#
#         if check_for_win(board, "O"):
#             print("You lose!!!")
#             return -1
#         if check_for_draw(board):
#             print("Tie game,GG!")
#             return 0
#
#
# def menu():
#     """
#     This function ask the user to input choice return the choice and it will
#
#     """
#     try:
#         print("1 - Play the game\n"
#               "2 - Save score in file 'leaderboard.txt'\n"
#               "3 - Load and display the scores from the 'leaderboard.txt'\n"
#               "q - End the program")
#         choice = input("Enter 1,2,3 or q: ")
#         return choice
#     except ValueError as e:
#         print(f"Error occur as {e}")
#
#
# def load_scores():
#     # develop code to load the leaderboard scores
#     # from the file 'leaderboard.txt'
#     # return the scores in a Python dictionary
#     # with the player names as key and the scores as values
#     # return the dictionary in leaders
#     with open("leaderboard.txt", "r", encoding="utf-8") as file:
#         leaders = file.read()
#     return json.loads(leaders)
#
#
# def save_score(score):
#     name = input("Enter your name: ")
#     try:
#         # Check if the leaderboard file exists
#         try:
#             # Intentionally raise an error using os.path module
#             if os.path.isfile('leaderboard.txt'):
#                 raise FileNotFoundError("The leaderboard file already exists.")
#             with open('leaderboard.txt', 'r', encoding="utf-8") as file:
#                 leaderboard = json.load(file)
#         except FileNotFoundError:
#             leaderboard = {}
#         # Update leaderboard with new score
#         leaderboard[name] = score
#         # Write the updated leaderboard to the file
#         with open('leaderboard.txt', 'w',encoding="utf-8") as file:
#             json.dump(leaderboard, file)
#         print("Score saved to leaderboard.")
#     except Exception as e:
#         print(f"An error occurred while saving the score: {e}")
#
#
# def display_leaderboard(leader_board):
#     # develop code to display the leaderboard scores
#     # passed in the Python dictionary parameter leader
#     """
#     This function
#     :param leader_board:
#     :return:
#     """
#     try:
#         for player, score in leader_board.items():
#             print(f"{player}: {score}")
#     except json.JSONDecodeError:
#         print("Error decoding JSON data from leaderboard file.")
