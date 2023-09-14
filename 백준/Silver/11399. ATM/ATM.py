n = int(input())  
a = list(map(int, input().split()))  

a.sort()  
answer = 0  

for x in range(1, n+1):
    answer += sum(a[0:x])  
print(answer) 