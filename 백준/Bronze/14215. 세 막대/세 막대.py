num = list(map(int, input().split()))
num.sort()
if num[0] + num[1] > num[2]:
    print(sum(num))
else:
    print(num[0] + num[1] + (num[0] + num[1] - 1))