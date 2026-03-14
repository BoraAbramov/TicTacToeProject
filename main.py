from curses.ascii import isdigit


def create_board():
    '''

    :return: list with length as _size
    '''
    _size = 9
    board = []
    for i in range(_size):
        board.append(i + 1)
    return board

def print_board(_board):
    '''

    :param _board: it a list
    :return: print the list, every 3 indexes
    '''
    for i in range(0, 3, 6):
        print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
        print("----------")
        print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
        print("----------")
        print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
        print("----------")

def get_move(player, board):
    while True:
        move = int(input(f"{player} please select your move: "))
        try:
            int(move)
        except Exception as e:
            print("invalid move")
            continue
        if 1 <= move <= 9 and board.index(move - 1) != player_change(symbol, symbol2):
            board[move - 1] = player
            print(board)


def player_change(symbol, symbol2):
    if symbol == "❌":
        player = symbol2
    else:
        player = symbol
    return player

def check_winner(board, player):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in win:



def board_check(player_move):
    if _board[player_move] != int:
        return False
    else:
        return True


while True:
    board = create_board()
    print_board(board)

    symbol = "❌"
    symbol2 = "⭕"
    _count = 0

    while _count < len(board):
        player = player_change(symbol, symbol2)
        get_move(player, board)