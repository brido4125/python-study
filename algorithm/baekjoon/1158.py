# 요시푸스 문제
N, K = map(int, input().split(' '))

num_list = [i for i in range(1, N + 1)]
answer_list = []

for i in range(N):
    k_index = K - 1
    if len(num_list) >= K:
        answer_list.append(num_list[k_index])
        del num_list[k_index]
        front_list = num_list[:k_index]
        lear_list = num_list[k_index:]
        num_list = lear_list + front_list
    elif len(num_list) == 1:
        answer_list.append(num_list[0])
    else:
        target = num_list[K - len(num_list) - 1]
        answer_list.append(target)
        num_list.remove(target)
    print(answer_list)

print(num_list)
