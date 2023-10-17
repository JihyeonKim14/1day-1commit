def solution(arr):
    m = min(arr)
    arr.remove(m)
    if len(arr) <= 1:
        answer = [-1]
    else:
        answer = arr
    return answer