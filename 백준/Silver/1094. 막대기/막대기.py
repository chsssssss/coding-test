X = int(input())
stick = 64
sticks = [64]
result = 0
while stick > 0:
    stick = stick // 2
    sticks.append(stick)
for s in sticks:
    if s <= X:
        result += 1
        if s == X:
            break
        X -= s
        
print(result)