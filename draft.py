

#index = 0  1  2  3  4  5  6  7  8
_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, 3, 6):
    print(f"{_board[i]} | {_board[i + 1]} | {_board[i + 2]}")
    print("----------")
    print(f"{_board[i + 3]} | {_board[i + 4]} | {_board[i + 5]}")
    print("----------")
    print(f"{_board[i + 6]} | {_board[i + 7]} | {_board[i + 8]}")
    print("----------")