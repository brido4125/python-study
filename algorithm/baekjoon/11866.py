from collections import deque

N,K = map(int, input().split())

dq = deque()
for i in range(1,N+1):
    dq.append(i)
target_index = K -1

answer = []

while len(dq) >= K:
    answer.append(dq[target_index])
    dq.remove(dq[target_index])
    for _ in range(target_index):
        popleft = dq.popleft()
        dq.append(popleft)

while len(dq) != 0:
    mod = K % len(dq)
    answer.append(dq[mod-1])
    dq.remove(dq[mod-1])
    for _ in range(mod-1):
        popleft = dq.popleft()
        dq.append(popleft)

print('<',end='')
for i in range(len(answer) - 1):
    print(answer[i],end=', ')
print(answer[len(answer) - 1],end='')
print('>')