import sys

N = int(sys.stdin.readline())

height = []
weight = []

for _ in range(N):
    x,y = map(int, sys.stdin.readline().split(' '))
    weight.append(x)
    height.append(y)

same_list = []
bigger_list = []
smaller_list = []

smaller = 0
bigger = 0
count = 0
for i in range(N):
    for j in range(N):
        if i == j:
            #본인 중복 제외
            count += 0
        elif weight[i] > weight[j] and height[i] > height[j]:
            #i가 덩치가 더 큰 경우
            bigger += 1
        elif weight[i] < weight[j] and height[i] < height[j]:
            #덩치가 더 작은 경우
            smaller += 1
        else:
            #비교 불가
            count += 1
    same_list.append(count)
    bigger_list.append(bigger)
    smaller_list.append(smaller)
    count = 0
    bigger = 0
    smaller = 0
