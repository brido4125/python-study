from collections import deque

dq = deque()

num = int(input())
#큐에다가 숫자 넣기
for i in range(1,num+1):
    dq.append(i)
#n-1번 만큼 숫자 빼기
for i in range(num-1):
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])