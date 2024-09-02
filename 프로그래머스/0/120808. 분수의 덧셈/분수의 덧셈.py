def solution(numer1, denom1, numer2, denom2):
    denom = 0
    if(denom1 == denom2):
        denom = denom1
    else:
        for i in range(min(denom1, denom2), 0, -1):
            if(denom1 % i == 0 and denom2 % i == 0):
                denom = denom1 * denom2 // i
                print(denom)
                break
                
        if(denom == 0):
            denom = denom1 * denom2
    numer = (denom//denom1) * numer1 + (denom//denom2) * numer2
    
    gcd_value = gcd(numer, denom)
    
    numer //= gcd_value
    denom //= gcd_value
    
    answer = [numer, denom]
    return answer 

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a