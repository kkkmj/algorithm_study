"""<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오."""
from collections import deque
dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]

n=int(input())
cube=[]
visited=[]
answer=[]
for _ in range(n):
    cube.append(list(map(int, input())))
    visited.append([False]*n)

def bfs(node,t):
    que=deque()
    que.append(node)
    answer.append(1)

    while que:
        x,y=que.popleft()
        for k in range(4):
            dxx,dyy=x+dx[k], y+dy[k]
            if -1<dxx<n and -1<dyy<n and cube[dxx][dyy]==1 and visited[dxx][dyy]==False:
                visited[dxx][dyy]=True
                que.append((dxx,dyy))
                answer[t]+=1

t=0
for i in range(n):
    for j in range(n):
        if cube[i][j]==1 and visited[i][j]==False:
            visited[i][j]=True
            bfs((i,j),t)
            t+=1

answer.sort()
print(len(answer))
for a in answer:
    print(a)


"""
주변을 구하는거라서 bfs로 구하는게 맞다고 생각해서 bfs로 풀었는데 다른사람의 풀이를 보니 dfs로 구현하는게 더 빨라서 dfs로도 풀어봤음
"""