import sys

board = [[[0] * 21 for _ in range(21)] for _ in range(21)]


def w(a, b, c):
    # 하나라도 0보다 작으면
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # 하나라도 20보다 크면
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif board[a][b][c] != 0:
        return board[a][b][c]
    elif a < b < c:
        board[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        board[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return board[a][b][c]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({a}, {b}, {c}) = {answer}".format(a=a, b=b, c=c, answer=w(a, b, c)))
