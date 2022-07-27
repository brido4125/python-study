# N -> 세로, M -> 가로
N, M = map(int, input().split(" "))

board = [list(map(str, input())) for _ in range(N)]


for col in range(0, N - 7):
    for row in range(0, M - 7):
        countW = 0
        countB = 0
        for i in range(col,col+8):
            for j in range(row,row+8):
                if board[0][0] == 'B':
                    if board[i][j] != 'W':
                        countW += 1
                    if board[i][j] != 'B':
                        countB += 1
                else:
                    if board[i][j] != 'W':
                        countB += 1
                    if board[i][j] != 'B':
                        countW += 1




