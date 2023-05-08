from collections import deque
import sys
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, m = map(int, input().split())
iced_area = [list(map(int, input().split())) for _ in range(n)]


def down_bfs(coordinate, visited):
    que = deque()
    que.append(coordinate)
    while que:
        x, y = que.popleft()
        visited[x][y]=True
        area0 = iced_area[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1<nx<n and -1<ny<m:
                if iced_area[nx][ny]==0 and not visited[nx][ny] and area0!=0:
                    area0-=1
                if iced_area[nx][ny]!=0 and not visited[nx][ny]:
                    que.append((nx, ny))
                    visited[nx][ny]=True
        iced_area[x][y]=area0




ice_num=-1
year=0

while ice_num<2:
    ice_num = 0
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if iced_area[i][j]!=0 and not visited[i][j]:
                down_bfs((i, j), visited)
                ice_num+=1
    year+=1
    if ice_num==0:
        print(0)
        sys.exit()

print(year-1)


"""
이정도면 나쁘지 않다! 한방에 골4 맞췃음! 효율도 나쁘지 않고
+로 visited로 한방에 값 바꿔주는 것 까지도 좋았음ㅎㅎ
 
다만 여기서 아쉬운 점은
어차피 두덩이 갈라지는 곳을 탐색하는 것이기 때문에 bfs자체가 거의 한번만 수행하게 됨.
그래서 굳이 2중 for문으로 0이 아닌 곳을 매번 탐색해줄 필요는 없음.

+로 덩이가 딱 나눠질때 끝내는게 아니라, 덩이를 나누고, 또 bfs해서 내려가게 하는 것까지 한다음에=불필요한 연산이 한번 더 추가가됨
그래서 이걸 방지하기 위해 
맨 처음에 그래프를 한번 탐색해줌. 그다음 빙하가 있는 곳을 tuple list에다 추가해줌.
그래서 for 문으로 그 리스트를 bfs함수에다가 넣어주면 됨.
또, 이런식으로 


"""