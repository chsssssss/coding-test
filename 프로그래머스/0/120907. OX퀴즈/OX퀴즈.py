def solution(quiz):
    answer = []
    for i in quiz:
        expr = i.replace(" ", "").split('=')
        if eval(expr[0]) == int(expr[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer