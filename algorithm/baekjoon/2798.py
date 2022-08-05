N,M = map(int, input().split())

num_list = list(map(int, input().split()))

answer_list = []

sum = 0
cnt = 0

for i in range(len(num_list)-2):
    sum += num_list[i]
    cnt += 1
    for j in range(i+1,len(num_list)-1):
        sum += num_list[j]
        cnt += 1
        for k in range(j+1,len(num_list)):
            sum += num_list[k]
            cnt += 1
            if sum <= M:
                answer_list.append(sum)
            sum -= num_list[k]
        sum -= num_list[j]
    sum -= num_list[i]

print(max(answer_list))
