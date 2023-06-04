import sys
input = sys.stdin.readline
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

r, c, t = map(int, input().split())
areas = [list(map(int, input().split())) for _ in range(r)]

visited = [[False]*c for _ in range(r)]
cleaner=[]


for _ in range(t):

    temp=[[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            if areas[i][j]==-1:
                cleaner.append((i, j))
            if areas[i][j]>4:
                near=0
                for k in range(4):
                    nx , ny = i + dx[k], j + dy[k]
                    if -1<nx<r and -1<ny<c and areas[nx][ny]!=-1:
                        temp[nx][ny]+=areas[i][j]//5
                        near+=1
                temp[i][j]-= (areas[i][j]//5)*near

    for i in range(r):
        for j in range(c):
            areas[i][j]+=temp[i][j]


    botX, botY = cleaner.pop()
    for i in range(botX+1, r-1):
        areas[i][0]=areas[i+1][0]

    for j in range(c-1):
        areas[r-1][j] = areas[r-1][j+1]

    for i in range(r-1, botX, -1):
        areas[i][c-1] = areas[i-1][c-1]

    for j in range(c-1, 1, -1):
        areas[botX][j] = areas[botX][j-1]
    areas[botX][1]=0

    botX, botY = cleaner.pop()
    for i in range(botX-1, 0, -1):
        areas[i][0] = areas[i-1][0]

    for j in range(c - 1):
        areas[0][j] = areas[0][j + 1]

    for i in range(botX):
        areas[i][c-1] = areas[i+1][c-1]
    for j in range(c - 1, 1, -1):
        areas[botX][j] = areas[botX][j - 1]
    areas[botX][1]=0

total = 0
for i in range(r):
    total += sum(areas[i])

print(total+2)