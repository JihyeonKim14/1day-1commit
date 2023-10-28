def solution(numbers):
    temp = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            temp.append(numbers[i] + numbers[j])
    result = []        
    for value in temp:
        if value not in result:
            result.append(value)
    result.sort()
    answer = result
    return answer