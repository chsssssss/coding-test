N, C = map(int, input().split())
numbers = list(map(int, input().split()))
dic = {}
result = []
for i in range(N):
    if numbers[i] in dic:
        dic[numbers[i]] += 1
    else:
        dic[numbers[i]] = 1
for num, count in sorted(dic.items(), key= lambda x: x[1], reverse=True):
    for _ in range(count):
        result.append(num)

print(' '.join(map(str, result)))