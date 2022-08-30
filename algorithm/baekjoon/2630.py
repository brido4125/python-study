N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0


# x,y는 색종이의 좌측 상단 점
def divideAndConquer(x, y, n):
    global blue, white
    if n < 1:
        return
    # n by n 만큼의 색종이가 있는지 확인
    first_pixel = board[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if first_pixel != board[i][j]:
                divideAndConquer(x, y, int(n / 2))
                divideAndConquer(x, y + int(n / 2), int(n / 2))
                divideAndConquer(x + int(n / 2), y, int(n / 2))
                divideAndConquer(x + int(n / 2), y + int(n / 2), int(n / 2))
                return
    # 해당 라인 아래로는 first_pixel과 board가 동일하다는 것
    # 즉, 온전한 하나의 색종이라는 의미
    if first_pixel == 0:
        white += 1
        return
    else:
        blue += 1
        return

divideAndConquer(0, 0, N)

print(white)
print(blue)
