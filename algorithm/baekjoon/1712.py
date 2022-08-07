A, B, C = map(int, input().split(' '))

count = 1

if B >= C:
    count = -1
else:
    count = A // (C - B)
    count += 1
print(count)


