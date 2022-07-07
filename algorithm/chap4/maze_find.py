import sys
from collections import deque

N, M = map(int, input().split())

maze = [[0] * M for _ in range(N)]

for i in range(N):
    readline = sys.stdin.readline()
    for j in range(M):
        maze[i][j] = readline[j]

dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

dq = deque()


def bfs():
    answer = 0
    check = [[False] * M for _ in range(N)]
    check[0][0] = True
    dq.append((0, 0, 1))
    while dq:
        x,y,d= dq.popleft()
        if y == N -1 and x == M -1:
            return d
        nextD = d + 1
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < M and 0 <= nextY < N:
                if maze[nextY][nextX] == '1':
                    if not check[nextY][nextX]:
                        check[nextY][nextX] = True
                        dq.append((nextX, nextY,nextD))


print(bfs())
