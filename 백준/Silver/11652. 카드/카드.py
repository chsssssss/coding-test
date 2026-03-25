N = int(input())
dic = {}
result = float('inf')
count = 0

for _ in range(N):
    num = int(input())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

for (key, val) in dic.items():
    if val > count:
        count = val
        result = key
    elif val == count:
        result = min(result, key)
print(result)