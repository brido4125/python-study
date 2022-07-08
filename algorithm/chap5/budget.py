import sys

N = int(input())
budget_list = list(map(int, sys.stdin.readline().split()))
M = int(input())

lo = 0
high = max(budget_list)
mid = (lo + high) // 2
answer = 0



def is_possible(mid):
    return sum(min(elem, mid) for elem in budget_list) <= M


while lo <= high:
    if is_possible(mid):
        lo = mid + 1
        answer = mid
    else:
        high = mid - 1
    mid = (lo + high) // 2  #

print(answer)
