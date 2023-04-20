"""미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다."""

from collections import deque
dx, dy = [1, 0, -1, 0], [0, 1,0, -1]

n, m = map(int, input().split())
miro = []

for ind in range(n):
    data = input()
    miro.append([])
    for i in data:
        miro[ind].append(int(i))



def isgo(x, y):
    return -1<x<n and -1<y<m and miro[x][y]==1

# def dfs(now, answer):
#     x, y = now
#     if x == n - 1 and y == m - 1:
#         ans.append(answer)
#         answer=0
#     for i in range(4):
#         dxx=x+dx[i]
#         dyy=y+dy[i]
#         if isgo(dxx,dyy):
#             visited[dxx][dyy]=True
#             dfs((dxx,dyy),answer+1)

def bfs(now):
    que = deque()
    que.append(now)

    while que:

        x,y=que.popleft()

        for i in range(4):
            dxx=x+dx[i]
            dyy=y+dy[i]
            if isgo(dxx,dyy):
                miro[dxx][dyy]=miro[x][y]+1
                que.append((dxx,dyy))

    return miro[n-1][m-1]



print(bfs((0,0)))

"""
그 길을 가면서 +1을 하는방식을 좀 생각해보자
보통 이런 문제 대부분 갔던 길 전 +1 로 함
"""