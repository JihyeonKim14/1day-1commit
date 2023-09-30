n = int(input())

# 약수 구하기
arr = []
sum = 0
for i in range(2,int(n ** 0.5) +1 ):
    while n % i == 0:
        arr.append(i)
        n = n//i

if n != 1:
    arr.append(n)


print(len(arr))
print(*arr)
