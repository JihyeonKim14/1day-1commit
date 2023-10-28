def solution(n, m):
    import math
    
    answer = []
    answer.append(math.gcd(n,m))
    answer.append(n*m//math.gcd(n,m))
    return answer