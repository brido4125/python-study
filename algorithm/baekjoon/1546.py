N = int(input())
score_list = list(map(int, input().split()))

M = max(score_list)

for i in range(len(score_list)):
    priv = score_list[i]
    score_list[i] = priv / M * 100

avg = sum(score_list) / len(score_list)

print(avg)