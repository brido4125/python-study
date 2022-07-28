N = int(input())
num_list = list(map(int, input().split()))


def get_max(target):
    max_value = -100_000_0
    for i in range(len(target)):
        if target[i] >= max_value:
            max_value = target[i]
    return max_value


def get_min(target):
    min_value = 100_000_0
    for i in range(len(target)):
        if target[i] <= min_value:
            min_value = target[i]
    return min_value


print(get_min(num_list),get_max(num_list))
