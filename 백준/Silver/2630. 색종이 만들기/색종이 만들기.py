N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def divide(x, y, size):
    global white, blue
    color = paper[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != color:
                half = size // 2
                divide(x, y, half)  # 1사분면
                divide(x, y + half, half)  # 2사분면
                divide(x + half, y, half)  # 3사분면
                divide(x + half, y + half, half)  # 4사분면
                return  # 더 이상 진행하지 않고 리턴

    # 모두 같은 색이라면
    if color == 0:
        white += 1
    else:
        blue += 1


divide(0, 0, N)
print(white)
print(blue)