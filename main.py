
def create_board():
    '''

    :return: list with length as _size
    '''
    _size = 9
    board = []
    for i in range(_size):
        board.append(i + 1)
    return board

def print_board(board):
    '''

    :param _board: it a list
    :return: print the list, every 3 indexes
    '''
    for i in range(0, 3, 6):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        print("----------")
        print(f"{board[i + 3]} | {board[i + 4]} | {board[i + 5]}")
        print("----------")
        print(f"{board[i + 6]} | {board[i + 7]} | {board[i + 8]}")
        print("----------")

def get_move(player, board):
    while True:
        move = int(input(f"{player} please select your move: "))
        try:
            int(move)
        except Exception as e:
            print("invalid move")
            continue
        index = move - 1
        if 0 < index < 10 and board.index(index) != player_change(symbol, symbol2):
            board[index] = player
            return board


def player_change(symbol, symbol2):
    if symbol == "❌":
        player = symbol2
    else:
        player = symbol
    return player

def check_winner(board, player, win):
    for x in win:
        for _ in x:
            if board[_] == player:
                print(f"{player} win")
            winner = player
    return winner

def score(winner, symbol, symbol2):
    score_table = {"❌": 0, "⭕": 0}
    if winner == symbol:
        score_table[symbol] = + 1
    else:
        score_table[symbol2] = + 1
    return score_table


while True:
    board = create_board()
    print_board(board)

    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    symbol = "❌"
    symbol2 = "⭕"
    _count = 0

    while _count < len(board):
        player = player_change(symbol, symbol2)
        get_move(player, board)
        check_winner(board, player, win)
        print_board(board)
        player_change(symbol, symbol2)
        _count += 1

    score()
    restert = input('if you play again, press enter: ')
    if restert == "":
        continue
    else:
        break