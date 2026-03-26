
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
    :param board: it a list
    :return: print the list, every 3 indexes
    '''
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("----------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("----------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("----------")


def get_move(player, board):
    '''
    :param player: the current player symbol
    :param board: the game board
    :return: updated board
    '''
    while True:
        try:
            move = int(input(f"{player} please select your move (1-9): "))
        except Exception as e:
            print("invalid move")
            continue
        index = move - 1
        if 0 <= index <= 8 and board[index] != (symbol and symbol2):
            board[index] = player
            return board
        else:
            print("invalid move")


def player_change(current_player):
    '''
    :param current_player: the current player symbol
    :return: the other player symbol
    '''
    if current_player == symbol:
        return symbol2
    else:
        return symbol


def check_winner(board, player, win):
    '''
    :param board: the game board
    :param player: the current player symbol
    :param win: list of winning combinations
    :return: player symbol if won, None otherwise
    '''
    for x in win:
        if board[x[0]] == board[x[1]] == board[x[2]] == player:
            print(f"{player} win!")
            return player
    return None


def update_score(winner, score_table):
    '''
    :param winner: the winning player symbol
    :param score_table: the current score dictionary
    :return: updated score table
    '''
    score_table[winner] += 1
    return score_table


win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
symbol = "❌"
symbol2 = "⭕"
score_table = {symbol: 0, symbol2: 0}

while True:
    board = create_board()
    print_board(board)

    current_player = symbol
    winner = None
    _count = 0

    while _count < len(board):
        get_move(current_player, board)
        winner = check_winner(board, current_player, win)
        print_board(board)

        if winner:
            update_score(winner, score_table)
            break

        current_player = player_change(current_player)
        _count += 1

    if not winner:
        print("It's a tie!")

    print(f"Score: {symbol} = {score_table[symbol]} | {symbol2} = {score_table[symbol2]}")

    restart = input('if you play again, press enter: ')
    if restart == "":
        continue
    else:
        break