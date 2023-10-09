def solution(x):
    sum = 0
    y = x
    while x > 0 :
        sum += x%10
        x = x//10
    if y % sum == 0:
        answer = True
    else:
        answer = False
        
    return answer