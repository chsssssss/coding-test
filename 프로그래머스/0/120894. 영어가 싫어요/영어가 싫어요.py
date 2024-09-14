def solution(numbers):
    answer = ''
    num = {"zero" : 0, "one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    word = ''
    for i in range(0, len(numbers)):
        if word in list(num.keys()):
            answer += str(num[word])
            word = ''
        word += numbers[i]
    answer += str(num[word])
    return int(answer)