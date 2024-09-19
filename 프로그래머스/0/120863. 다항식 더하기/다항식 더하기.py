def solution(polynomial):
    answer = ''
    x = 0
    num = 0
    for i in polynomial.split(" "):
        if 'x' in i:
            if i[0] == 'x':
                x += 1
            else:
                x += int(i[:-1])
        elif i.isdigit():
            num += int(i)
            
    if x > 0:
        if x == 1:
            answer = 'x'
        else:
            answer = f'{x}x'
            
    if num > 0:
        if answer:
            answer += f' + {num}'
        else:
            answer = str(num)

    
    return answer