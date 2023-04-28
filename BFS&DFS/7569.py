"""창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토에 인접한 곳은 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지 그 최소 일수를 알고 싶어 한다.

토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다."""
from collections import deque

dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
m, n, h = map(int, input().split())
box = [[] for _ in range(h)]
for i in range(h):
    box[i] = [list(map(int, input().split())) for _ in range(n)]


def bfs(que):
    while que:
        x, y, z = que.popleft()
        day = box[x][y][z]
        for k in range(6):
            dxx, dyy, dzz = x + dx[k], y + dy[k], z + dz[k]
            if -1 < dxx < h and -1 < dyy < n and -1 < dzz < m and box[dxx][dyy][dzz] != -1 and box[dxx][dyy][dzz] != 1:
                if box[dxx][dyy][dzz]==0:
                    box[dxx][dyy][dzz]=day+1
                    que.append((dxx, dyy, dzz))
                else:
                    box[dxx][dyy][dzz] =min(day + 1, box[dxx][dyy][dzz])

que = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                que.append((i,j,k))
bfs(que)
day = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            day = max(day, box[i][j][k])

print(day - 1)

"""
결국 그냥 반례 케이스 보고 수정했음..ㅠ 일단 여러개가 있을 수 있기 때문에 하나씩 돌리면서 que인경우를 할게 아니라 que를 여러개 담은 다음에 
접근해야함
근데,,,, 이딴게 bfs..?ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
bfs로 푼게 맞는지도 잘 모르겠다 그리고 속도도 너무 느림
할때 마다 bfs가 아니라 for문으로 dxdy 이렇게 하는것같은데 과연 이게 제대로 푸는게 맞을까..?
"""