N, K = map(int, input().split())

num_list = list(map(int, input()))

answer = []

count = K

for elem in num_list:
    while answer and count > 0 and answer[-1] < elem:
        answer.pop()
        count -= 1
    answer.append(elem)

#주어진 배열이 내림차순으로 정렬된 경우
if count > 0:
    for i in range(count):
        answer.pop()

for e in answer:
    print(e, end="")

