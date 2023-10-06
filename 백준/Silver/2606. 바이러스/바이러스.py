def dfs(idx):
    global visited, graph, answer
    visited[idx] = True
    answer +=1

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


N = int(input())
M = int(input())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N + 1)
answer = 0

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = True
    graph[y][x] = True

dfs(1)

print(answer - 1)