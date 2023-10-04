def solution(x, n):
    if x > 0:
        answer = list(range(x,x*n+1, x))
    if x < 0:
        answer = list(range(x, x*n-1, x))
    if x == 0:
        answer = [0] * n
    return answer