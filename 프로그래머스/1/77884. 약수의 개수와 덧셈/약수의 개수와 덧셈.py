def solution(left, right):
    sum = 0
    for val in range(left, right + 1):
        check = 0
        for i in range(1, val+1):
            if val % i == 0:
                check += 1
            
        if check % 2 == 0:
            sum += val
        else:
            sum -= val        
        
        
                
        '''     
        if check % 2 == 0:
            sum += val
        else:
            sum -= val
        '''
    return sum