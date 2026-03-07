
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

def get_move(player, _board)
    while True:
        player = input("Enter your move 1-9: ")
        if player.isdigit():
            player = int(player)
        if 1 <= player <= 9:
            return player
        else:
            continue

def board_update():




while True:
    _board = create_board()

    while True:
        player = current_player
        player_move = valid_input
        player_input = ready_for_board
        board_check(player_input)
        board_update(player_input)
        check_conditions = winner_tie
        print_board(_board)
        _end = check_end

_summery = resault_restart