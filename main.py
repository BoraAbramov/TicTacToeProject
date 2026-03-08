
def create_board():
    #יוצר את הרשימה להדפסת הלוח
    _size = 9
    board = []
    for i in range(_size):
        board.append(i + 1)
    return board

def print_board(_board):
    #מדפיס את הרשימה בצורת לוח 3 על 3
    for i in range(0, 3, 6):
        print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
        print("----------")
        print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
        print("----------")
        print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
        print("----------")

def valid_input():
    while True:
        player = input("Enter your move 1-9: ")
        if player.isdigit():
            player = int(player)
        if 1 <= player <= 9:
            return player
        else:
            continue

def board_check(player_move):
    if _board[player_move] != int:
        return False
    else:
        return True




while True:
    _board = create_board()

    player = "❌"

    while True:
        player_move = valid_input()

        board_check(player_move)

        board_update(player_move)

        check_conditions = winner_tie()

        print_board(_board)

        _end = check_end()

        switch_player()

    _summery = resault_restart()
print()