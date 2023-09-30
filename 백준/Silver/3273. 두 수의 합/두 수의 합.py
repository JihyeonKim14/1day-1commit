''' 완탐
n = int(input())

arr = list(map(int,input().split()))
sum = int(input())
cnt = 0
for i,a in enumerate(arr):
    for j,b in enumerate(arr):
        if i == j:
            continue
        if a + b == sum:
            cnt += 1
cnt = cnt/2

print(int(cnt))
'''

n = int(input())

arr = sorted(list(map(int,input().split())))

answer = int(input())

s = 0
e = n-1
cnt = 0
while s < e:
    if arr[s] + arr[e] == answer:
        cnt += 1

    if arr[s] + arr[e] > answer:
        e -= 1 
    else:
        s += 1
print(cnt)
    