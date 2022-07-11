# 이항 계수2
import sys

N, K = map(int, input().split(" "))

MOD = 10007
sys.setrecursionlimit(10 ** 7)

cache = [[0] * 1001 for _ in range(1001)]

def bino(n, k):
    if cache[n][k] != 0:
        return cache[n][k]
    if k == 0 or k == n:
        cache[n][k] =  1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino(n - 1, k)
    return cache[n][k]


print(bino(N, K) % MOD)