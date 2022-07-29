import sys

N = int(input())

order_list = [list(map(str,sys.stdin.readline().split())) for _ in range(N)]

my_stack = []

for elem in order_list:
    if elem[0] == 'push':
        my_stack.append(int(elem[1]))
    elif elem[0] == 'pop':
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack.pop())
    elif elem[0] == 'size':
        print(len(my_stack))
    elif elem[0] == 'empty':
        if len(my_stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(my_stack) == 0:
            print(-1)
        else:
            print(my_stack[-1])










