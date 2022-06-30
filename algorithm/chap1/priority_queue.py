#Priority Queue => Heap 사용(이진 트리)
#Python -> Min Heap : 트리의 최상단 노드에 제일 작은값
import heapq

pq = []
heapq.heappush(pq,6)
heapq.heappush(pq,12)
heapq.heappush(pq,-7)
heapq.heappush(pq,222)
heapq.heappush(pq,0)

print(pq)
while pq:
    print(pq[0])
    heapq.heappop(pq)

