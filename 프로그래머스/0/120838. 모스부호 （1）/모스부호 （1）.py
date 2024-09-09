def solution(letter):
    answer = ''
    alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    letter = letter.split(' ')
    m = {}
    a = 97
    
    for i in alphabet:
        m[i] = chr(a)
        a += 1
    
    for i in letter:
        answer += m[i]

    return answer