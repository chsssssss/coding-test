def solution(numbers, k):
    answer = 0
    numbers = numbers * 500
    cnt = 0
    i = 0
    while cnt < k:
        answer = numbers[i]
        i += 2
        cnt += 1
        
    return answer