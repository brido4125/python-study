import sys

T = int(sys.stdin.readline())

answer = 0

for _ in range(T):
    N = int(sys.stdin.readline())
    dic = {}
    for __ in range(N):
        name, kind = map(str, sys.stdin.readline().split())
        try:
            dic[kind] += 1
        except KeyError as e:
            dic[kind] = 2 # 입지않는 경우까지 포함
    values = list(dic.values())
    total = 1
    for elem in values:
        total *= elem
    answer = total - 1 #마지막에 입지 않는 경우 제외
    print(answer)
