from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    doc = deque()
    A = map(int, input().split())
    for idx, value in enumerate(A):
        doc.append((idx, value))
    answer = 0
    while True:
        X = [d[1] for d in doc]
        index = doc[0][0]
        value = doc[0][1]
        if value != max(X):
            temp = doc.popleft()
            doc.append(temp)
        else:
            answer += 1
            if index == M:
                print(answer)
                break
            temp = doc.popleft()