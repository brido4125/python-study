# N -> 세로, M -> 가로
N, M = map(int, input().split(" "))

# 가로 반복 횟수 : (M - 7)
# 세로 반복 횟수 : (N - 7)

board = [list(map(str, input())) for _ in range(N)]

answer_list = []

for p in range(N - 7):
    for q in range(M - 7):
        cnt = 0
        start = board[p][q]
        for i in range(p, p + 8):
            for j in range(q, q + 8):
                if start == 'B':
                    if (i + j) % 2 == 0: #짝수번째
                        if board[i][j] == 'W':
                            cnt += 1
                    else:
                        if board[i][j] == 'B':
                            cnt += 1
                elif start == 'W':
                    if (i + j) % 2 == 0: #짝수번째
                        if board[i][j] == 'B':
                            cnt += 1
                    else:
                        if board[i][j] == 'W':
                            cnt += 1
        if cnt > 32:
            added = cnt - 32
            cnt = 32 - added

        answer_list.append(cnt)

print(min(answer_list))

