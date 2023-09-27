def recur(number):
    if len(arr) == M:
        print(*arr)
        return
    
    for i,num in enumerate(num_list):
        if num not in arr:
            arr.append(num)
            recur(i+1)
            arr.pop()

N , M = map(int,input().split())
num_list = list(map(int,input().split()))
num_list.sort()

arr = []
recur(1)
