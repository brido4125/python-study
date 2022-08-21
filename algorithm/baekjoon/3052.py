num_list = list(int(input()) for _ in range(10))

answer_list = []

for elem in num_list:
    mod = elem % 42
    if mod not in answer_list:
        answer_list.append(mod)


print(len(answer_list))
