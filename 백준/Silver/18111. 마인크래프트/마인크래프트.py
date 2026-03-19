N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

height_count = [0] * 257

for row in blocks:
    for h in row:
        height_count[h] += 1

time = float("inf")
height = 0

for h in range(257):
    add = 0
    remove = 0

    for i in range(257):
        if i > h:
            remove += (i - h) * height_count[i]
        else:
            add += (h - i) * height_count[i]

    if remove + B >= add:
        t = remove * 2 + add

        if t < time or (t == time and h > height):
            time = t
            height = h

print(time, height)