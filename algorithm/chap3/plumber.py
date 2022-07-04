N, L = map(int, input().split())

leek_points = []
for i in map(int, input().split()):
    leek_points.append(i)

fixed_condition = []
for i in range(0, N):
    fixed_condition.append(False)

leek_points.sort()

count = 0
for i in range(0, N):
    if not fixed_condition[i]:
        fixed_condition[i] = True
        tape_length = abs(leek_points[i] - 0.5) + L
        count += 1
        for j in range(i + 1, N):
            if leek_points[j] <= tape_length:
                fixed_condition[j] = True
            elif leek_points[j] > tape_length:
                break
    else:
        continue

print(count)
