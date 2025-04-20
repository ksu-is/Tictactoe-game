# tic_tac_toe.py

import random

def print_board(board):
    print("\nCurrent board:")
    for row in board:
        print("+---+---+---+")
        print("| " + " | ".join(row) + " |")
    print("+---+---+---+")

def check_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(name, board):
    while True:
        try:
            move = int(input(f"{name}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] not in ['X', 'O']:
                return row, col
            else:
                print("Cell already taken, choose another.")
        except (ValueError, IndexError):
            print("Invalid input, enter a number from 1 to 9.")

def get_ai_move(board):
    available_moves = [(r, c) for r in range(3) for c in range(3) if board[r][c] not in ['X', 'O']]
    return random.choice(available_moves)

def play_game():
    board = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]

    mode = input("Enter number of players (1 or 2): ")
    while mode not in ['1', '2']:
        mode = input("Invalid input. Enter 1 for single player, 2 for two players: ")

    if mode == '2':
        player1 = input("Enter name for Player 1 (X): ")
        player2 = input("Enter name for Player 2 (O): ")
    else:
        player1 = input("Enter your name (X): ")
        player2 = "AI"

    current_player, current_symbol = player1, 'X'

    while True:
        print_board(board)

        if current_player == "AI":
            row, col = get_ai_move(board)
        else:
            row, col = get_move(current_player, board)

        board[row][col] = current_symbol

        if check_winner(board, current_symbol):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = player2 if current_player == player1 else player1
        current_symbol = 'O' if current_symbol == 'X' else 'X'

if __name__ == "__main__":
    play_game()
