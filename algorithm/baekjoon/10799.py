input_list = list(map(str, input()))

cur_pipe = 0
count = 0
stack = []
for i in range(len(input_list)):
    if input_list[i] == ')':
        if input_list[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1
    elif input_list[i] == '(':
        stack.append(input_list[i])

print(count)

