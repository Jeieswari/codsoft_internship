import math

# Board initialization
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Function to check if the game is won
def check_winner(player):
    win_cond = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columns
        [0, 4, 8], [2, 4, 6]             # Diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_cond)

# Check if the board is full
def is_full():
    return all(cell != ' ' for cell in board)

# Minimax Algorithm
def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    elif check_winner('X'):
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI Move
def ai_move():
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'


def play_game():
    print("Welcome to Tic-Tac-Toe! You are 'X' and AI is 'O'")
    print_board()

    while True:
        
        move = int(input("Enter your move (1-9): ")) - 1
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if check_winner('X'):
            print("You win!")
            break
        if is_full():
            print("It's a draw!")
            break

        
        print("AI is making a move...")
        ai_move()
        print_board()

        if check_winner('O'):
            print("AI wins!")
            break
        if is_full():
            print("It's a draw!")
            break


play_game()
