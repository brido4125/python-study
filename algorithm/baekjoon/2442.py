N = int(input())

for i in range(1,2*N,2):
    print(" " * (((2*N-1) - i) // 2),end="")
    print("*" * i)

