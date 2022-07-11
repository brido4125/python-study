N = int(input())
fibo_list = [-1 for _ in range(N + 1)]


def fibo(num):
    if fibo_list[num] == -1:
        if num == 0:
            fibo_list[0] = 0
            return 0
        elif num == 1:
            fibo_list[1] = 1
            return 1
        fibo_list[num] = fibo(num - 1) + fibo(num - 2)
        return fibo(num - 1) + fibo(num - 2)
    else:
        if num == 0:
            return fibo_list[0]
        elif num == 1:
            return fibo_list[1]
        return fibo_list[num - 1] + fibo_list[num - 2]


print(fibo(N))
