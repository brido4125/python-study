import sys

MOD = 10_007

sys.setrecursionlimit(10 ** 7)
N = int(input())

cache = [0 for _ in range(1001)]
cache[1] = 1
cache[2] = 2


def func(num):
    if cache[num] != 0:
        return cache[num]
    cache[num] = func(num - 1) + func(num - 2)
    return cache[num]


print(func(N) % MOD)
