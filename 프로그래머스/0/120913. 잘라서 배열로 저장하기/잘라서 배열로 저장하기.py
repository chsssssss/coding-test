def solution(my_str, n):
    answer = []
    text = ''
    for i in range(0, len(my_str)):
        text += my_str[i]
        if (i+1) % n == 0:
            answer.append(text)
            text = ''
        elif i == len(my_str) - 1:
            answer.append(text)
    return answer