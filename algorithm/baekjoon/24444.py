import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

# 인덱스 살릴려면 N+1로 그래프 구현
board = [[] for _ in range(N + 1)]

visited = [0] * (N+1)

# 인접 행렬이 아닌 인접 리스트로 그래프 구현 => 메모리 부족
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

for i in range(N + 1):
    board[i].sort() # 오름차순으로 정렬 -> 오름차순 순서로 sort

queue = deque([R])
visited[R] = 1


def bfs():
    count = 2
    while queue:
        popleft = queue.popleft()
        for elem in board[popleft]:
            if visited[elem] == 0:
                queue.append(elem)
                visited[elem] = count
                count += 1


bfs()
for i in visited[1::]:
    print(i)