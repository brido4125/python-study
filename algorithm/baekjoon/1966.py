import sys
from collections import deque

N = int(input())

for _ in range(N):
    x, target_index = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        max_value = max(queue)
        front = queue.popleft()
        target_index -= 1

        if front == max_value:
            count += 1
            if target_index == -1:
                print(count)
                break
        else:  # max보다 front 값이 작으면
            queue.append(front)
            if target_index < 0:
                target_index = len(queue) - 1
