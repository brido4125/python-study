A, B, V = map(int, input().split(' '))

answer = 0

distance = A - B

mod = (V - B) % distance
answer = (V - B) // distance

if mod != 0:
    answer += 1

print(answer)




