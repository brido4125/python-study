N = int(input())

board = [list(map(int, input().split(' '))) for _ in range(N)]

white = 0
blue = 0


def divideAndConquer(x, y, n):
    global blue, white
    sameColor = board[x][y]#좌측 최상단
    for i in range(x, x + n):
        for j in range(y, y + n):
            if sameColor != board[i][j]:
                divideAndConquer(x, y, n // 2)
                divideAndConquer(x, y + n // 2, n // 2)
                divideAndConquer(x + n // 2, y, n // 2)
                divideAndConquer(x + n // 2, y + n // 2, n // 2)
                return
    if sameColor == 0:
        white += 1
        return
    else:
        blue += 1
        return


divideAndConquer(0, 0, N)
