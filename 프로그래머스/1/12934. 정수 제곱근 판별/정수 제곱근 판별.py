def solution(n):
    answer = 0
    for i in range(1, int(n**0.5) + 1):
        if i**2 == n:
            answer = (i+1) ** 2
        else:
            answer = -1
    return answer