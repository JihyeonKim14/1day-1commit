def solution(n):
    n = str(n)
    temp = []
    for i in range(len(n)):
        temp.append(int(n[len(n)-1-i]))
        
    answer = temp
    return answer