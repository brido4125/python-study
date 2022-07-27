import sys

M, N = map(int, input().split(' '))

board = [[0] * N for _ in range(M)]

for i in range(M):
    s = input()
    for j in range(N):
        board[i][j] = s[j]

count = (M - 7) * (N - 7)



