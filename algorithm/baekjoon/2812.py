N, K = map(int, input().split(' '))

num_list = list(map(int, input()))

cnt = 0

# 찾은 최대값의 앞에 놓인 정수가 제거야할 정수 갯수보다 작으면 max 값은 2번째 max 값 사용
while cnt < K:
    #print("num_list = ", num_list)
    sorted_list = sorted(num_list)
    #print("sorted_list = ", sorted_list)
    for i in range(len(sorted_list) - 1, -1, -1):
        max_value = sorted_list[i]
        #print("max_value = ",max_value)
        max_index = num_list.index(max_value)
        #print("max_index = ", max_index)
        if K - cnt > max_index:
            break
    if max_index == 0:
        if max_value == max(num_list):
            for j in range(len(num_list)):
                if num_list[j] == max_value:
                    real_max_index = j
            num_list.remove(min(num_list[max_index:real_max_index]))
        elif max_value < max(num_list):
            real_max_index = num_list.index(max(num_list))
            num_list.remove(min(num_list[max_index:real_max_index]))
        else:
            num_list.remove(min(num_list[max_index:]))
    else:
        num_list.remove(min(num_list[:max_index]))
    cnt += 1

for i in range(len(num_list)):
    print(num_list[i],end="")


