N = int(input())    # 재료의 개수
M = int(input())    # 갑옷이 완성되는 번호의 합
ingredients = list(map(int, input().split()))
ingredients.sort()
count = 0
start_idx = 0
end_idx = N - 1
while start_idx < end_idx:
    if ingredients[start_idx] + ingredients[end_idx] == M:
        count += 1
        start_idx += 1
        end_idx -= 1
    elif ingredients[start_idx] + ingredients[end_idx] < M:
        start_idx += 1
    else:
        end_idx -= 1
print(count)