
def create_board():
    _size = 9
    board = []
    for i in range(_size):
        board.append(i + 1)
    return board

def print_board(_board):
    for i in range(0, 3, 6):
        print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
        print("----------")
        print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
        print("----------")
        print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
        print("----------")



while True:
    _board = create_board()
    print_board(_board)

    1player_move_2player_move
    board_update
    resault_check

    start_stop
