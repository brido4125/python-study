N = int(input())

cnt = 0
target = 665

while cnt != N:
    target += 1
    if str(target).find('666') != -1:
        cnt += 1
        answer = target

print(answer)
