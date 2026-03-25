import sys

nums = sys.stdin.read().split()
n = int(nums[0])
numbers = nums[1:n+1]
result = []

for num in numbers:
    result.append(int(num[::-1]))
result.sort()

for i in result:
    print(i)