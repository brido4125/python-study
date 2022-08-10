N = int(input())

start = N


def get_sum(num):
    sum = 0
    for elem in str(num):
        sum += int(elem)
    return sum

answer = 0

for target in range(N):
    # target의 부분합 구하기
    sum = get_sum(target)
    if target + sum == N:
        answer = target
        break

print(answer)


