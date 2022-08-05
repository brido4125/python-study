import sys
from collections import deque

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())

apple_list = [list(map(int,sys.stdin.readline().split())) for _ in range(K)]

L = int(sys.stdin.readline())

dir_list = [list(sys.stdin.readline().split()) for _ in range(L)]

snake_len = 1
timer = 0

board = [[0 for j in range(N)] for i in range(N)]

for elem in apple_list:
    board[elem[0]-1][elem[1]-1] = 'a'

dq = deque()

print(apple_list)
print(dir_list)