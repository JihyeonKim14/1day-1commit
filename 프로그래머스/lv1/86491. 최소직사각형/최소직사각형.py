def solution(sizes):
    max_val = 0
    max_val2 = 0
    for card in sizes:
        temp = max(card)
        card.remove(temp)
        if temp >= max_val:
            max_val = temp
    for card2 in sizes:
        temp2 = max(card2)
        if temp2 >= max_val2:
            max_val2 = temp2
            
        
        
    answer = max_val * max_val2
    return answer 
