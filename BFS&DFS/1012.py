from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

def bfs(ground, x, y):
    que = deque()
    ground[x][y]=0
    que.append((x,y))

    while que:

        a, b = que.popleft()
        for po in range(4):
            dxx = a + dx[po]
            dyy = b + dy[po]
            if -1<dxx<n and -1<dyy<m and ground[dxx][dyy]==1:
                ground[dxx][dyy]=0
                que.append((dxx,dyy))
    return

for _ in range(t):
    worm = 0
    m, n, k = map(int, input().split())
    ground = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        ground[x][y]=1

    for i in range(n):
        for j in range(m):
            if ground[i][j]==1:
                bfs(ground, i, j)
                worm += 1

    print(worm)


