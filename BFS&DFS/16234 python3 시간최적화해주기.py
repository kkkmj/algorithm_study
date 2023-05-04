import sys
#import time
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

n, l, r = map(int, sys.stdin.readline().split())

countries=[]
for _  in range(n):
    countries.append(list(map(int, sys.stdin.readline().split())))
    visited = [[-1 for _ in range(n)] for _ in range(n)]

#start = time.time()
def bfs(node):
    a, b = node
    union=[(a,b)]
    total=countries[a][b]

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
                    total+=p2
                    union.append((dxx, dyy))
                    visited[dxx][dyy]=move
    if total!=countries[a][b]:
        num = int(total/len(union))
        for x, y in union:
            countries[x][y] = num
move=0
while True:

    k=0
    for i in range(n):
        for j in range(n):
            if visited[i][j]!=move:
                visited[i][j]=move
                bfs((i,j))
                k+=1
    if k==n*n:
        break

    move+=1
#end=time.time()
print(move)
#print(end-start)
"""
일단 시간초과가 났던 이유는
맨 처음 연합을 구한 다음에 for문 끝나고 인구수를 다시 재분배 하는 식으로 했음
이유1. 연합과 연합사이가 이미 닫혀있기 때문에 bfs에서 사람수를 나눠도 됐는데, 이미 visited도 해서 상관 없는데 이것때문에 값이 바껴서 영향을 줄까봐 걱정
이것도 있었고, 연합을 구한 다음에, 해도 될거라고 생각했기 때문.
근데 어차피 상관 없기도 했고, 인구를 재분배 하는 것 자체가 이중for문이라서 비효율적임.
암튼 그래서 bfs함수 내에서 인구를 재분배해줄 수 있음.

암튼 여기서 고민인거
1. visited함수를 매번 초기화 하지 않고 값으로 하는게 과연 좋은 것인가? - boolean값과, int값 or 매번 초기화
2. union을 굳이 전역 list로 만들어서 할 필요가 있나? < 근데 얘가 시간복잡도에 차이가 있나?
3. 사람 이동을 bfs 함수내에서가 아닌 bfs함수 끝나고 할 필요가 있나? (아무리 생각해도 결국 sum은 sum대로 빠져나와서 해줘야 되기 때문에 이득이 아닐 것 같은데
"""

