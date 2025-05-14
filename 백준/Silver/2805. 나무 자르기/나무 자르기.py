N, M = map(int, input().split())
H = list(map(int, input().split()))
start = 0
end = max(H)
answer = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for h in H:
        if h > mid:
            total += h - mid
    if total >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
print(answer)