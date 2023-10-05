def solution(s):
    a = []
    num = list(s.split())
    temp = [int(x) for x in num]
    
    answer = f'{min(temp)} {max(temp)}'
    return answer