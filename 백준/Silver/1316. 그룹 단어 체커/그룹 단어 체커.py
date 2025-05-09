N = int(input())
result = 0
for _ in range(N):
    word = input()
    group = [word[0]]
    before = word[0]
    isGroup = True
    for i in range(1, len(word)):
        if before != word[i]:
            if  word[i] not in group:
                group.append(word[i])
            else:
                isGroup = False
                break
        before = word[i]
    if isGroup:
        result += 1
print(result)