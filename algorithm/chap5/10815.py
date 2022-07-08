import sys

N = int(input())
card_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
number_list = list(map(int, sys.stdin.readline().split()))

answer = [0 for _ in range(M)]

card_list.sort()


def binary_search(num):
    lo = 0
    high = len(card_list) - 1
    mid = (lo + high) // 2
    while lo <= high:
        if num < card_list[mid]:
            high = mid - 1
        elif num > card_list[mid]:
            lo = mid + 1
        else:
            return True
        mid = (lo + high) // 2


for i in range(M):
    if binary_search(number_list[i]):
        answer[i] = 1

for elem in answer:
    print(str(elem) + " ", end="")
