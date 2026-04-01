def solution(numbers, target):
    answer = 0
    return dfs(numbers, 0, 0, target, answer)

def dfs(numbers, idx, number, target, count):
    if idx == len(numbers):
        if target == number:
            return 1
        else:
            return 0
    
    return dfs(numbers, idx + 1, number + numbers[idx], target, count) + dfs(numbers, idx + 1, number - numbers[idx], target, count)