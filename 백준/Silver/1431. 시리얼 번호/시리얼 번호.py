N = int(input())
numbers = []
for _ in range(N):
    num = input()
    numbers.append(num)
numbers.sort(key= lambda x: (len(x), sum(int(c) for c in x if c.isdigit()), x))

for i in numbers:
    print(i)