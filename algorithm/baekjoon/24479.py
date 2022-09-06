import sys

sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, sys.stdin.readline().split())

adj_list = []
for _ in range(N + 1):
    adj_list.append([])

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj_list[x].append(y)
    adj_list[y].append(x)

for elem in adj_list:
    elem.sort(reverse=True)

visited = [False] * (N + 1)

answer = [0] * (N + 1)

cnt = 0


def dfs(start_node):
    global cnt
    visited[start_node] = True
    cnt += 1
    # 기존에는 max(answer)+1을 answer에 넣는 로직 => 시간 초과 => arrayList는 순회에는 불리한 자료구조
    answer[start_node] = cnt
    for node in adj_list[start_node]:
        if not visited[node]:
            dfs(node)


dfs(R)

for i in range(1, len(answer)):
    print(answer[i])
