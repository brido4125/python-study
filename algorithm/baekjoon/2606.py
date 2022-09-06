import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

visited = [False] * (N + 1)

# 1번을 통해서 걸리는 바이러스의 수니까, 1번은 제외하기 위해서 -1로 시작
answer = -1


def dfs(start_node):
    global answer
    visited[start_node] = True
    answer += 1
    for node in adj_list[start_node]:
        if not visited[node]:
            dfs(node)


dfs(1)
print(answer)
