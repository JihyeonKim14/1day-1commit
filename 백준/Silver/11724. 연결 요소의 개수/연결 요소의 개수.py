import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(idx):
    global graph, visited, answer
    visited[idx] = True

    for i in range(1, N+1):
        if not visited[i] and graph[idx][i]:
            dfs(i)

N, M = map(int, input().split())
graph = [[False] *(N+1) for _ in range(N+1)]
visited = [False] * (N+1)
answer = 0

for i in range(M):
    u,v = map(int,input().split())
    graph[u][v] = True
    graph[v][u] = True

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        answer +=1

print( answer)