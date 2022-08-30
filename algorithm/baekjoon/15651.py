# 중복 순열 구하기

N, M = map(int, input().split())

num_list = []
answer = []

for i in range(N):
    num_list.append(i + 1)

for i in range(M):
    answer.append(-1)


def backTracking(L):
    if L == M:
        for elem in answer:
            print(elem, end=' ')
        print()
    else:
        for i in range(N):
            answer[L] = num_list[i]
            backTracking(L + 1)


backTracking(0)
