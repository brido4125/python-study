import sys
import heapq

N = int(input())

number_list = []

for _ in range(N):
    heapq.heappush(number_list, int(sys.stdin.readline()))

answer = 0

while True:
    try:
        start = heapq.heappop(number_list) + heapq.heappop(number_list)
        heapq.heappush(number_list, start)
        answer += start
    except IndexError as e:
        break

print(answer)