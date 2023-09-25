N, K = map(int, input().split())

arr = list(map(int,input().split()))

prefix = [0] * (N+1)
answer = []

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

for j in range(K,N+1):
    temp = prefix[j] - prefix[j - K]
    answer.append(temp)

print(max(answer))