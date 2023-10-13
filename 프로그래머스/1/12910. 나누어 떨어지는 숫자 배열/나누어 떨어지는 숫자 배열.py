def solution(arr, divisor):
    answer = []
    cnt = 0
    for val in arr:
        if val % divisor == 0 :
            answer.append(val)
            cnt += 1
    
    if cnt == 0:
        answer = [-1]
    answer.sort()
    return answer