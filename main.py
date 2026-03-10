
def create_board():
#crete a board - _size addition for maybe change
#Return list of board size
    _size = 9
    board = []
    for i in range(_size):
        board.append(i + 1)
    return board

def print_board(_board):
#print _board as board
    for i in range(0, 3, 6):
        print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
        print("----------")
        print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
        print("----------")
        print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
        print("----------")

def get_move(player, board):
    move = input("please select a move: ")
    if move in board:
        board[move] = player
        return board
    else:
        print("invalid move")

def check_winner(board, player):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win:



def board_check(player_move):
    if _board[player_move] != int:
        return False
    else:
        return True




while True:
    _board = create_board()

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