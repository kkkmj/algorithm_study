from collections import deque

n, m = map(int, input().split())
graphs = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graphs[u].append(v)
    graphs[v].append(u)

visited = [False]*(n+1)

def bfs(node):
    que = deque()
    que.append(node)

    while que:
        x = que.popleft()
        for i in graphs[x]:
            if not visited[i]:
                visited[i]=True
                que.append(i)

# def dfs(node):
#     visited[node]=True
#
#     for i in graphs[node]:
#         if not visited[i]:
#             dfs(i)
answer = 0
for i in range(1,n+1):
    if not visited[i]:
        if not graphs[i]:
            answer+=1
            visited[i]=True
        else:
            visited[i]=True
            bfs(i)
            answer+=1

print(answer)

"""
1. dfs로 풀면 안됨
2. bfs로 하면 시간초과날 확률이 큼
그래서 union find써야됨
"""