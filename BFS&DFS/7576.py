"""
창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.
"""
from collections import deque

dx=[1, 0, 0, -1]
dy=[0, 1, -1, 0]

day = 0
m, n = map(int, input().split())
que = deque()
tomatoes = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if tomatoes[i][j]==1:
            que.append((i,j))

def bfs():
    while que:
        x, y = que.popleft()
        for po in range(4):
            dxx = x + dx[po]
            dyy = y + dy[po]
            if -1<dxx<n and -1<dyy<m and tomatoes[dxx][dyy]==0:
                tomatoes[dxx][dyy]=tomatoes[x][y]+1
                que.append((dxx,dyy))

bfs()

for i in range(n):
    for j in range(m):
        if tomatoes[i][j]==0:
            print(-1)
            exit(0)
        day=max(day, tomatoes[i][j])
print(day-1)


"""
풀었는데 bfs로 안풀었고 시간초과가 나서 결국 답보고 했음

bfs가 뭔지 제대로 알아야 되기도 하고,
날짜를 실행 횟수만큼 하는게 아니라, 어차피 0인지 아닌지만 판별하는것 밖에 없어서 거의
그냥 숫자를 뿔려나간다는 생각을 못했음...
문제를 많이 풀어봐야되는 이유
암튼 bfs 가 모든 경로를 하나씩 탐색 해가면서 여러발로 하는 것 처럼
얘도 그냥 한번 탐색하고 할 필요 없이, 한번 확산이 되는게 하루 지나는 거기 때문에
이 확산만 제대로 생각하면 풀 수 있는 문제임
단순히 확산 + 날짜를 +1로 해서 답을 구해주는 것
..... 생각을 좀 더 해봐야 되기 보다는 이런건 그냥 문제 여러개 풀어봐서 감 익히는거 말곤 없는듯
걍 문제 여러번 풀고 하반기를 노리자..ㅎㅎ 면접은 그래도 몇번은 보는 걸 목표로 하고
"""