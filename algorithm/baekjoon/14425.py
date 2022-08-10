import sys

N, M = map(int, sys.stdin.readline().split())

input_set = []

for _ in range(N):
    input_set.append(sys.stdin.readline())

target_list = []

for _ in range(M):
    target_list.append(sys.stdin.readline())


count = 0

for target in target_list:
    if target in input_set:
        count += 1

print(count)