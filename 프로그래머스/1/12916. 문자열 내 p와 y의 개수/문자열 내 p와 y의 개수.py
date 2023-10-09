def solution(s):
    arr = [x.upper() for x in s]
    print(arr)
    p = arr.count('P')
    y = arr.count('Y')
    
    if p == y:
        answer = True
    else:
        answer = False

    return answer