N = int(input())
n = 1   # 현재 대각선 번호
limit = 1   # 대각선의 마지막 번호

while limit < N:
    limit += n + 1
    n += 1

# 대각선 내 위치 계산
a = n - (limit - N)

if n % 2 == 0:
    print(f"{a}/{n - a + 1}")
else:
    print(f"{n - a + 1}/{a}")