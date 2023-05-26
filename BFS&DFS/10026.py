from collections import deque
n = int(input())
areas = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(node, color, flag):
    que = deque()
    que.append(node)
    a,b=node
    if flag:
        areas[a][b]='R'

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1<nx<n and -1<ny<n and not visited[nx][ny]:
                if areas[nx][ny]==color:
                    if flag:
                        areas[nx][ny]='R'
                    visited[nx][ny]=True
                    que.append((nx, ny))

no, yes = 0, 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            flag = 0
            visited[i][j]=True
            if areas[i][j]=='G':
                flag = 1
            bfs((i, j), areas[i][j], flag)
            no+=1

visited = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            flag = 0
            visited[i][j]=True
            bfs((i, j), areas[i][j], flag)
            yes+=1

print(no, yes)

