import random
import os.path
import json
random.seed()

def draw_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*11)


def welcome(board):
    print("Welcome to the 'Unbeatable Noughts and Crosses' game.");
    draw_board(board);

def initialise_board(board):
    # develop code to set all elements of the board to one space ''
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j]=''
    return board
    
def get_player_move(board):
     while True:
        move = input("choose your square: \n 1 2 3 \n 4 5 6 \n 7 8 9:  ")
        try:
            index = int(move)-1
            row = index // 3
            col = index % 3
            if 0<=index<=8 and board[row][col]=="":
                board[row][col] = 'X'
                return row, col
            else:
                print("The spot is already taken")
        except ValueError:
            print("please enter only integer from 1 to 9")

def choose_computer_move(board):
     while True:
        row = random.randint(0,2)
        col = random.randint(0,2)
        if board[row][col] == "":
            board[row][col] = 'O'
            return row, col


def check_for_win(board, mark):
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for row in board:
        if all(cell==mark for cell in row):
            return True
    
    for col in range(3):
        if all (board[row][col]==mark for row in range(3)):
            return True
    
    if all(board[i][i]==mark for i in range(3)) or all(board[i][2-i]==mark for i in range(3)):
      return True  
    
    return False

def check_for_draw(board):
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    for row in board:
        if any(cell=='' for cell in row):
            return False
    
    return True
        
def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        row, col = get_player_move(board)
        draw_board(board)
        if check_for_win(board, 'X'):
            print("You won!")
            return 1
        # if not check for a draw by calling check_for_draw(board)
        elif check_for_draw(board):
            print("The game is a draw.")
            return 0
        # if not, then call choose_computer_move(board)
        # to choose a spot for the computer
        row, col = choose_computer_move(board)
        draw_board(board)
        # if computer won
        if check_for_win(board, 'O'):
            print("You lost!")
            return -1
        # prints "draw" if the game is draw
        elif check_for_draw(board):
            print("Draw.")
            return 0
                    
                
def menu():
    while True:
        choice = input(
            "Enter one of the following options: \n1 - Play the game\n2 - Save score in leaderboard\n3 - Load and display the leaderboard\nq - End the program\n1,2,3 or q?: ")
        if choice in ['1', '2', '3', 'q']:
            return choice

def load_scores():
    if os.path.exists("leaderboard.txt"):
        try:
            with open("leaderboard.txt", 'r') as file:
                leaders = json.load(file)
                return leaders
        except json.decoder.JSONDecodeError:
            print("Error: The file 'leaderboard.txt' does not contain valid JSON data.")
            return {}
        except Exception as e:
            print(f"An error occurred while loading the leaderboard: {e}")
            return {}
    else:
        print("Error: The file 'leaderboard.txt' does not exist.")
        return {}
 
    
def save_score(score):
    name = input("Enter your name: ")
    leaders = load_scores()
    leaders[name] = score
    with open('leaderboard.txt', 'w') as f:
        json.dump(leaders, f)

    return


def display_leaderboard(leaders):
    if leaders:
        print("\nLeaderboard:")
        print("Name\t\tScore")
        for name, score in leaders.items():
            print(f"{name}\t\t{score}")
    else:
        print("Leaderboard is empty.")
    pass

