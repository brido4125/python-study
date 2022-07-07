import sys

sys.setrecursionlimit(10 ** 6)#이거 넣어줘야함
N, M = map(int, input().split())

adj = [[0] * N for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    adj[a][b] = adj[b][a] = 1

answer = 0
check = [False] * N


def dfs(now):
    for nxt in range(N):
        if adj[now][nxt] and not check[nxt] :
            check[nxt] = True
            dfs(nxt)


for i in range(N):#N개의 노드만큼 check 배열 순회
    if not check[i]:
        answer += 1
        check[i] = True
        dfs(i)

print(answer)
