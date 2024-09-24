def solution(num, total):
    avg = total // num
    
    if num % 2 == 0:
        start = avg - (num // 2) + 1
    else:
        start = avg - (num // 2)
    
    return [start + i for i in range(num)]