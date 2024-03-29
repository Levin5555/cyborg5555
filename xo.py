import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if the game is over (win or draw)
def is_game_over(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # Check for a draw (no empty spaces left)
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return True

    return False

# Function to calculate the score of the board
def calculate_score(board):
    # If 'X' wins, return -1
    if any(board[i][j] == 'X' for i in range(3) for j in range(3)):
        return -1
    # If 'O' wins, return 1
    if any(board[i][j] == 'O' for i in range(3) for j in range(3)):
        return 1
    # It's a draw
    return 0

# Function to find the optimal move using the A* algorithm
def find_optimal_move(board, depth, maximizing_player):
    if is_game_over(board):
        return calculate_score(board)

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = find_optimal_move(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = find_optimal_move(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to make the AI's move using the A* algorithm
def ai_move(board):
    best_move = None
    best_eval = float('-inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_eval = find_optimal_move(board, 0, False)
                board[i][j] = ' '

                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)

    return best_move

# Main game loop
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        while True:
            try:
                row, col = map(int, input("Enter your move (row and column, e.g., '0 0'): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                    board[row][col] = 'X'
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter row and column as two integers.")

        # Check if player wins or it's a draw
        if is_game_over(board):
            print_board(board)
            if any(board[i][j] == 'X' for i in range(3) for j in range(3)):
                print("Congratulations! You win!")
            else:
                print("It's a draw!")
            break

        print_board(board)

        # AI player's move
        ai_row, ai_col = ai_move(board)
        print(f"AI's move: {ai_row} {ai_col}")
        board[ai_row][ai_col] = 'O'

        # Check if AI wins or it's a draw
        if is_game_over(board):
            print_board(board)
            if any(board[i][j] == 'O' for i in range(3) for j in range(3)):
                print("AI wins!")
            else:
                print("It's a draw!")
            break