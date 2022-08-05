import sys
from collections import deque

N = int(sys.stdin.readline())

dq = deque([])

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dq.append(command[1])
    elif command[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif command[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
    elif command[0] == 'pop':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)




