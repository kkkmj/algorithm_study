from collections import deque
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split()) #로봇청소기 좌표와, 방향
#방향은 0 북, 1 동, 2 남, 3 서
areas = [list(map(int, input().split())) for _ in range(n)] #0은 청소x, 1은 벽
clean = 0

while True:
    if areas[r][c]==0:
        areas[r][c]=-1
        clean +=1

    dirty_cnt=0
    for i in range(4):
        nx, ny = r + dx[i], c + dy[i]
        if -1<nx<n and -1< ny<m and areas[nx][ny]==0:
            dirty_cnt+=1
    if dirty_cnt==0:
        r = r + (dx[d]) * (-1)
        c = c + dy[d] * (-1)
        if -1<r<n and -1<c<m:
            if areas[r][c]!=1:
                continue
            else:
                break

    else:
        d-=1
        if d<0:
            d=3
        if -1<r+dx[d]<n and -1<c+dy[d]<m:
            if areas[r+dx[d]][c+dy[d]]==0:
                r = r + dx[d]
                c = c + dy[d]

print(clean)
