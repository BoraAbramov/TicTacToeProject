

_size = 9
_board = []
for i in range(_size):
    _board.append(i + 1)


for i in range(0, 3, 9):
    print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
    print("----------")
    print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
    print("----------")
    print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
    print("----------")


sahkan = "❌"
sahkan2 = "⭕"
_count = 0
win = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
player = sahkan

while _count < 9:
    move = int(input(f"{player} please select your move: "))
    if 1 <= move <= 9 and _board.index(move - 1) != player:
        _board[move - 1] = player
        print(_board)
    else:
        print("invalid move")
        continue


    for x in win:
        for _ in x:
            if _board[_] == player:
                print(f"{player} win")


    _count += 1

    if symbol == "❌":
        player = symbol2
    else:
        player = symbol

print('It`s a Tie')
