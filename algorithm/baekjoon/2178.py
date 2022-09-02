from collections import deque

N, M = map(int, input().split())

board = [list(map(int, input())) for _ in range(N)]

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

queue = deque([])
queue.append((0, 0))


def bfs():
    while queue:
        popleft = queue.popleft()
        x = popleft[0]
        y = popleft[1]
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if 0 <= nextX < M and 0 <= nextY < N and board[nextY][nextX] == 1:
                queue.append((nextX, nextY))
                board[nextY][nextX] = board[y][x] + 1


bfs()
print(board[N-1][M-1])
