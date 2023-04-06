"""
마법사 상어는 파이어볼, 토네이도, 파이어스톰, 물복사버그 마법을 할 수 있다. 오늘 새로 배운 마법은 비바라기이다. 비바라기를 시전하면 하늘에 비구름을 만들 수 있다. 오늘은 비바라기를 크기가 N×N인 격자에서 연습하려고 한다. 격자의 각 칸에는 바구니가 하나 있고, 바구니는 칸 전체를 차지한다. 바구니에 저장할 수 있는 물의 양에는 제한이 없다. (r, c)는 격자의 r행 c열에 있는 바구니를 의미하고, A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양을 의미한다.

격자의 가장 왼쪽 윗 칸은 (1, 1)이고, 가장 오른쪽 아랫 칸은 (N, N)이다. 마법사 상어는 연습을 위해 1번 행과 N번 행을 연결했고, 1번 열과 N번 열도 연결했다. 즉, N번 행의 아래에는 1번 행이, 1번 행의 위에는 N번 행이 있고, 1번 열의 왼쪽에는 N번 열이, N번 열의 오른쪽에는 1번 열이 있다.

비바라기를 시전하면 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생긴다. 구름은 칸 전체를 차지한다. 이제 구름에 이동을 M번 명령하려고 한다. i번째 이동 명령은 방향 di과 거리 si로 이루어져 있다. 방향은 총 8개의 방향이 있으며, 8개의 정수로 표현한다. 1부터 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 이다. 이동을 명령하면 다음이 순서대로 진행된다.

모든 구름이 di 방향으로 si칸 이동한다.
각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
구름이 모두 사라진다.
2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
"""

n, m = map(int, input().split())
dxp = [-1, -1, 0, 1, 1, 1, 0, -1]
dyp = [0, -1, -1, -1, 0, 1, 1, 1]
sky = []
cloud = [(n-1,0), (n-1,1), (n-2,0), (n-2,1)]
visited = [[False for _ in range(n)] for _ in range(n)]
for _ in range(n):
    sky.append(list(map(int, input().split())))

def move(di, si):
    for i in range(len(cloud)):
        dx, dy = cloud[i]
        for _ in range(si):
            dx += dyp[di-1]
            dy += dxp[di-1]
            if(dx<0):
                dx=n-1
            elif(dx>n-1):
                dx=0
            if(dy<0):
                dy=n-1
            elif(dy>n-1):
                dy=0
            """
            이부분
            dx = (dx + dyp[di-1] * si )%n
            이런식으로도 만들 수 있음 쩐당
            """
        cloud[i]=(dx, dy)
        visited[dx][dy]=True
        sky[dx][dy]+=1

def water_dup():
    for i in range(len(cloud)):
        water=0
        x, y = cloud[i]
        if x+1<n and y+1<n:
            if sky[x+1][y+1]>0:
                water += 1
        if x+1<n and y-1>-1:
            if sky[x+1][y-1]>0:
                water += 1
        if x-1>-1 and y-1>-1:
            if sky[x-1][y-1]>0:
                water += 1
        if x-1>-1 and y+1<n:
            if sky[x-1][y+1]>0:
                water += 1
        """
        여기도
        diagonal_row = [1,1,-1,-1]
        diagonal_col = [1,-1,1,-1]
        이거 먼저 선언해주고
        
        nrow = row + diagonal_row[i]
        ncol = col + diagonal_col[i]
        이렇게 더해준 다음
        if -1<x<n and -1<y<n:
            if sky[x-1][y-1] >0:
        이렇게 짜줄 수 있음"""

        sky[x][y]+=water
    cloud.clear()

def make_cloud():
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                visited[i][j] = False
                continue

            if(sky[i][j]>1):
                cloud.append((i,j))
                sky[i][j]-=2

            """여기도 굳이 이렇게 안하고
            방문 여부를 전역변수가 아닌 move에서 만들어서 초기화하는 방식으로 해주면 굳이 false로 바꿔주는 일을 할 필요가 없음
            이동하기 전에 항상 구름 방문 여부를 초기화시키기 때문
            그래서 그렇게 하면
            if visited[i][j]==False and sky[i][j]>1:
                cloud.append((i,j))
                
            이런식으로도 해줄 수 있음
            """

for _ in range(m):
    di, si = map(int, input().split())
    move(di, si)
    water_dup()
    make_cloud()

ans = 0
for w in sky:
    ans += sum(w)
print(ans)

"""
1. 리스트 인덱스 관리 잘해주기. 계속 리스트 인덱스 때문에 삐끗삐끗함 거의 한 90%가 리스트 인덱스 에러
그리고 범위 변수 에러ㅋㅋㅋㅋ 다 거기서 거기인것들

시간초과가 났는데 이유는 cloud를 삭제하고, 있던 곳에는 구름을 다시 생성하지 않고, 없던 곳에만 구름을 생성하는 코드에서
 visited를 안해주고 그냥 해당하는 위치변수값 찾아서 remove로 지우게 했는데
 아무래도 이중for문 안에 있는데다가 거기서 또 remove자체도 for문 이니 3중 for문이 돼서 시간초과가 난듯 하다.
 아무래도 remove등 이런 for문으로 안하고 탐색하는거 해줄 때는 방문 여부로 해서 해줘야 되는듯
 
 또 *n 으로 리스트 초기화해주면 얕은복사가 일어나서 모두 바뀌게 되니 주의해주자.
 또한, 아?마 1차원 배열이나 2차원배열이나 시간차이는 그렇게 안나는 듯 하다
 방문여부 1차원배열로 하려다 자꾸 접근 바보같이 해서 그냥 2차원배열로 했더니 걍 됐다 이건 좀 예상 외일지도..."""