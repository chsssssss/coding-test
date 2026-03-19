import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
numbers.sort()
count = 0
left = 0
right = n - 1

while left < right:
    sum = numbers[left] + numbers[right]

    if sum == x:
        count += 1
        left += 1
        right -= 1
    elif sum < x:
        left += 1
    else:
        right -= 1

print(count)