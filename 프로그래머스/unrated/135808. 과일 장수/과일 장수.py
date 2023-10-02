def solution(k, m, score):
    # score 정렬
    score.sort()
    answer = 0
    
    for i in range(len(score) // m):
        arr = []
        for j in range(m):
            arr.append(score[-1])
            score.pop()
        answer += min(arr) * m
        
    return answer