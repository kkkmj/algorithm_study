import sys
import time
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, l, r = map(int, sys.stdin.readline().split())

countries=[]
for _  in range(n):
    countries.append(list(map(int, sys.stdin.readline().split())))
    visited = [[-1 for _ in range(n)] for _ in range(n)]

start = time.time()
def bfs(node,k):
    que = deque()
    que.append(node)
    while que:
        x, y = que.popleft()
        p = countries[x][y]
        for i in range(4):
            dxx, dyy = x + dx[i], y+dy[i]
            if -1<dxx<n and -1<dyy<n and visited[dxx][dyy]!=move:
                p2 = countries[dxx][dyy]
                if l<=abs(p-p2)<=r:
                    que.append((dxx, dyy))
                    union[k].append((dxx, dyy))
                    total_num[k]+=p2
                    visited[dxx][dyy]=move
move=0
while True:
    union = []
    total_num=[]


    k=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=move:
                union.append([])
                visited[i][j]=move
                union[k].append((i,j))
                total_num.append(countries[i][j])
                bfs((i,j),k)
                k+=1
    if k==n*n:
        break
    for i in range(len(union)):
        num=int(total_num[i]/len(union[i]))
        for x, y in union[i]:
            countries[x][y]=num

    move+=1
end = time.time()
print(move)
print(end-start)

"""
1. 사실 시간 초과에 영향을 준게 크진 않았지만
visited를 굳이 매번 초기화해줄 필요 없이 이게 몇번째냐에 따라 해당되는지 안되는지로 방문 여부를 파악해줄 수 있다.
원래는 visited==False:로 매번 초기화 시켜줬었는데 그냥 방문 횟수에 따라서 visited값이 방문 횟수가 아니면 방문한것이 아니기 때문에 visited=False인거랑 동급의 효과를 가질 수 있음
visited를 자꾸 매번 초기화 시켜주려고 하는데 이런식으로 하지 말고 그냥 횟수에 따라서 알 수 있게 여부로 표시해주자.
이런식으로 방문 여부를 최대한 안쓰려고 하는게 중요한것 같음 (ex토마토 문제에서 값 자체를 날짜로 바꾼다거나 하는 등)

"""

