N , M = map(int,input().split())
num_list = sorted(list(map(int,input().split())))


arr = []

def recur(number):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(number, N):
        if num_list[i] not in arr:
            arr.append(num_list[i])
            recur(i+1)
            arr.pop()


recur(0)