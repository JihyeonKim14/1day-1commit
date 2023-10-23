def solution(price, money, count):
    sum = 0
    for i in range(1,count+1):
        sum += price * i
    
    temp = money - sum
    
    answer = -1
    if temp < 0 :
        answer = abs(temp)
    else:
        answer = 0
    

    return answer