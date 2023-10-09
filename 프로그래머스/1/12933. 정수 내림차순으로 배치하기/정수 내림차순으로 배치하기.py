def solution(n):
    n = str(n)
    arr = [int(x) for x in n]
    arr.sort(reverse =True)
    temp = ''
    for i in range(len(arr)):
        temp += str(arr[i])
    answer = int(temp)
    return answer