# Tic Tac Toe Game (Console Version)

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for combo in win_conditions:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw():
    return " " not in board

def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, choose position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = player
                break
            else:
                print("Position already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Choose a number from 1 to 9.")

def game_loop():
    current_player = "X"
    print("Tic Tac Toe Game")
    print("Positions are numbered 1 to 9:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        print_board()
        player_move(current_player)

        if check_winner(current_player):
            print_board()
            print(f"Player {current_player} wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

game_loop()
