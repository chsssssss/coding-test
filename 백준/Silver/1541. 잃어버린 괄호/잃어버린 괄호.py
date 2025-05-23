N = input().split('-')
answer = sum(map(int, N[0].split('+')))
for i in N[1:]:
    answer -= sum(map(int, i.split('+')))
print(answer)