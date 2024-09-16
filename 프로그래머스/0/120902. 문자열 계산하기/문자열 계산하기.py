def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i in range(1, len(my_string), 2):
        operator = my_string[i]
        number = int(my_string[i + 1])
        
        if operator == '+':
            answer += number
        elif operator == '-':
            answer -= number
    return answer