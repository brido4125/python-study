score_list = [list(map(int, input().split(' '))) for _ in range(5)]

total_score_list = []


def get_list_sum(target):
    sum = 0
    for i in range(len(target)):
        sum += target[i]
    return sum


for i in range(5):
    total_score_list.append(get_list_sum(score_list[i]))


def get_max(target):
    max_value = target[0]
    index = 0;
    for j in range(len(target)):
        if target[j] > max_value:
            max_value = target[j]
            index = j
    return index, max_value


answer = get_max(total_score_list)

print(answer[0]+1, answer[1])
