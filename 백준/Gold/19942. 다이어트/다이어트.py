def recur(idx, a,b,c,d,price):
    global answer
    global used
    global answer_used

    if a >= mp and b >= mf and c >= ms and d >= mv:
        if answer > price:
            answer = min(answer, price)
            answer_used = []
            
            for i in used:
                answer_used.append(i)
    if idx == n:
        return

    # 재료 썼을때
    used.append(idx + 1)
    recur(idx + 1, a + arr[idx][0], b + arr[idx][1], c + arr[idx][2], d + arr[idx][3], price + arr[idx][4])
    used.pop()

    #재료 안썼을때
    recur(idx + 1, a, b, c, d, price)


n = int(input())
arr = [[] for _ in range(n)]
temp = []
mp,mf,ms,mv = map(int, input().split())

for i in range(n):
    a,b,c,d,e = map(int, (input().split()))
    arr[i].append(a)
    arr[i].append(b)
    arr[i].append(c)
    arr[i].append(d)
    arr[i].append(e)

answer = 999999999999

used = []
answer_used = []

recur(0,0,0,0,0,0)

answer_used.sort()

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)