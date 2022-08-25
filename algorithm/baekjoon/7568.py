import sys

N = int(sys.stdin.readline())

height = []
weight = []

for _ in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    weight.append(x)
    height.append(y)

bigger_list = []

bigger = 0
for i in range(N):
    for j in range(N):
        if weight[i] < weight[j] and height[i] < height[j]:
            #덩치가 더 작은 경우
            bigger += 1
    bigger_list.append(bigger)
    count = 0
    bigger = 0
    smaller = 0

#print("big",bigger_list)

answer = [x+1 for x in bigger_list]

for elem in answer:
    print(str(elem) + " ",end="")