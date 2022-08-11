import sys
import heapq

N = int(input())

target_list = []

#python => default가 min heap이라서 max heap 사용하려면 아예 들어오는 값을 음수화 시켜서 사용
for _ in range(N):
    target = int(sys.stdin.readline())
    if target == 0:
        if len(target_list) == 0:
            print(0)
        else:
            print(-heapq.heappop(target_list))
    else:
        heapq.heappush(target_list, -target)
