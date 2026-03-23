import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = 0

for _ in range(N):
    height = int(input())
    count = 1

    # 1. 나보다 작은 애들 제거
    while stack and stack[-1][0] < height:
        result += stack[-1][1]
        stack.pop()

    # 2. 같은 키 처리
    if stack and stack[-1][0] == height:
        same_count = stack[-1][1]
        result += same_count
        stack.pop()
        count += same_count
        
        # 3. 뒤에 더 큰 애 있으면 +1
        if stack:
            result += 1

    else:
        # 4. 나보다 큰 애가 남아있으면 +1
        if stack:
            result += 1
    stack.append((height, count))

print(result)