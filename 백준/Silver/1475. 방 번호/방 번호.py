N = int(input())
numbers = [0] * 10
for i in str(N):
    if i == '6' or i == '9':
        numbers[6] += 1
    else:
        numbers[int(i)] += 1
numbers[6] = (numbers[6] + 1) // 2

print(max(numbers))