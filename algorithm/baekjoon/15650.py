# 사전순으로 증가하는 수열 구하기

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
            print(elem,end=' ')
        print()
    else:
        for i in range(N):
            if L >= 1:
                if answer[L-1] < num_list[i]:
                    answer[L] = num_list[i]
                else:
                    continue # 하위 코드 실행하지 않고 바로 다음번 반복문 실행
            else:
                answer[L] = num_list[i]
            backTracking(L+1)


backTracking(0)
        