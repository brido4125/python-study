import sys

N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]

print(adj)

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj[x - 1][y - 1] = 1
    adj[y - 1][x - 1] = 1

answer = 0
chk = [False * N]

for i in range(N):
    if not chk[i]:
        answer += 1
        chk[i] = True

