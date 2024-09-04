from datetime import datetime

def solution(age):
    answer = 0
    now_year = datetime.now().year
    answer = now_year - age - 1
    return answer