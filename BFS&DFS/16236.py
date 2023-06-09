from collections import deque
dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]

n = int(input())
shark_size = 2
shark=[]
eating = 0
time=0
areas = [list(map(int, input().split())) for _ in range(n)]

fishes = {i:deque() for i in range(1,7)}

for i in range(n):
    for j in range(n):
        if 0 < areas[i][j] < 7:
            fishes[areas[i][j]].append((i, j))
        if areas[i][j]==9:
            shark[0]=(i, j)

"""
그럼 걍
1. 공간이없다면 break
2. 물고기가 1마리면 먹으러 가기
3. 이상이면 물고기 탐색 함수


"""
fish_d=deque()
while True:
    help = True
    for i in range(1,shark_size):
        if len(fishes[i])!=0:
            help = False
        else:
            fish_d.append(fishes[i].pop)
    if help:
        break

que = deque(fishes[1])

while que:
    x, y = que.popleft()
    a,b = shark[0]
    while
    for i in range(4):

