from collections import deque
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
n = int(input())

area = [list(map(int, input().split())) for _ in range(n)]

def bfs(node, visited, k):
    que = deque()
    que.append(node)

    while que:
        x, y = que.popleft()
        for i in range(4):
            dxx, dyy = x + dx[i], y + dy[i]
            if -1<dxx<n and -1<dyy<n and area[dxx][dyy]>k and visited[dxx][dyy]==False:
                visited[dxx][dyy]=True
                que.append((dxx,dyy))

total=0
k=0

while True:
    visited=[[False]*n for _ in range(n)]
    t=0
    for i in range(n):
        for j in range(n):
            if area[i][j]>k and visited[i][j]==False:
                visited[i][j]=True
                bfs((i,j), visited,k)
                t+=1
    if t==0:
        break
    if total<=t:
        total=t
    k+=1
print(total)