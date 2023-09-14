N = int(input())

list = list(map(int,input().split()))

sum = 0
temp = 0

for val in list:
    temp = 0
    for i in range(val):
        if val % (i+1) == 0:
            temp +=1
    if temp == 2:
        sum+=1


print(sum)
