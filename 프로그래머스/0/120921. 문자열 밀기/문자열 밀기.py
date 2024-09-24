def solution(A, B):
    if A == B:
        return 0
    
    n = len(A)
    for i in range(n):
        rotated_A = ''.join(A[(j - i) % n] for j in range(n))
        if rotated_A == B:
            return i
    
    return -1