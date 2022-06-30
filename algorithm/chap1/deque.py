from collections import deque

#Doubled queue => thread-safe하지 않아서 알고리즘에서 사용
dq = deque()
dq.append(52)#뒤로 넣음
dq.appendleft(43)#앞으로 넣음
dq.pop()#뒤에서 뺌
dq.popleft()#앞에서 뺌
