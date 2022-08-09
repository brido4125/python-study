my_list = list(int(input()) for _ in range(9))

max_value = max(my_list)
print(max_value)
print(my_list.index(max_value)+1)