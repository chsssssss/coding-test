def solution(cipher, code):
    answer = ''
    for i in range(0, len(cipher) + 1):
        if i % code == 0 and i != 0:
            answer += cipher[i - 1]
    return answer