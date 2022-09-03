# PyPy3로 제출
N = int(input())

reculsive_cnt = 0
dynamic_cnt = 0


def reculsive_fibo(n):
    global reculsive_cnt
    if n < 3:
        reculsive_cnt += 1
        return 1
    else:
        return reculsive_fibo(n - 1) + reculsive_fibo(n - 2)


fibo = [0, 1, 1]


def dynamic_fibo(n):
    global dynamic_cnt
    if n < 3:
        return fibo[n]
    for i in range(3, n + 1):
        dynamic_cnt += 1
        fibo.append(fibo[i - 2] + fibo[i - 1])
    return fibo[-1]


reculsive_fibo(N)
dynamic_fibo(N)

print(reculsive_cnt,dynamic_cnt)
