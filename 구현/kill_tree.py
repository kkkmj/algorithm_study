#TODO 걍 제초제 로직 다시 짜야함 서순이 안맞아서 틀리는거임

n, m, k, c = map(int, input().split())
#n = 격자의 크기 m = 박멸이 진행되는 년 수, k = 제초제의 확산 범위, c = 제초제가 남아있는 년 수
tree = []

all_kill=0
#빈칸은 0, 벽은 -1
for _ in range(n):
    tree.append(list(map(int, input().split())))

def growth(visit):
    dxl = [1, 0, -1, 0]
    dyl = [0, 1, 0, -1]

    tree_f = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if(tree[i][j]<=0):
                continue
            cnt = 0
            cnt2 = 0
            for p in range(4):
                x=i+dxl[p]
                y=j+dyl[p]
                if 0<=x<n and 0<=y<n: #인접한 칸이 0~n사이인지
                    if tree[x][y]>0: #나무가 있는만큼 성장
                        cnt+=1
                    if tree[x][y]==0: #인접한게 없을때만 번식하게하기
                        cnt2+=1
            tree[i][j]+=cnt
            tree_f[i][j]=cnt2
            visit[i][j]=True
    return tree_f, visit


def expand(tree_f, visit):
    dxl = [1, 0, -1, 0]
    dyl = [0, 1, 0, -1]
    #여기서 for문을 두번 돌려서 인접한게 없는걸 찾아줄건지
    #아니면 그 위에서 인접한거 2차원배열을 또 만들어서 해줄지 (근데 어차피 시간복잡도 생각하면 공간복잡도 늘려서 시간복잡도 아끼는게 날듯? 그러기엔 공간복잡도도 ㅈㄴ적게주는뎁쇼..ㄷ)
    for i in range(n):
        for j in range(n):
            if (tree[i][j] > 0 and tree_f[i][j]!=0): #나무가 있거나, 주변에 자리가 있을때만
                tree_n=int(tree[i][j]/tree_f[i][j]) #나무/주변 개수만큼
                for p in range(4):
                    x=i+dxl[p]
                    y=j+dyl[p]
                    if 0<=x<n and 0<=y<n and visit[x][y]==False and tree[x][y]>=0:
                        #인접한 주변이 0~n사이이고, 비어있거나 나무여야 되고, 원래 있던 나무자리가 아니어야됨
                        tree[x][y] += tree_n #그럼 개수만큼 추가
# 나무가 없는 칸에 제초제를 뿌리면 박멸되는 나무가 전혀 없는 상태로 끝이 나지만,
# 나무가 있는 칸에 제초제를 뿌리게 되면 4개의 대각선 방향으로 k칸만큼 전파되게 됩니다.

# 단 전파되는 도중 벽이 있거나 나무가 아얘 없는 칸이 있는 경우,>이게 제초제가 있는경우를 포함하는게 아닌가보네
# 그 칸 까지는 제초제가 뿌려지며 그 이후의 칸으로는 제초제가 전파되지 않습니다.
# 제초제가 뿌려진 칸에는 c년만큼 제초제가 남아있다가 c+1년째가 될 때 사라지게 됩니다.
# 제초제가 뿌려진 곳에 다시 제초제가 뿌려지는 경우에는 새로 뿌려진 해로부터 다시 c년동안 제초제가 유지됩니다.
def find_kill():
    max_kill=0
    kx,ky=-1,-1
    for i in range(n):
        for j in range(n):
            if (tree[i][j] > 0): #나무가 있다면
                dxx = [1, 1, -1, -1]
                dyx = [1, -1, 1, -1]
                temp = max_kill
                sum_t = tree[i][j] #자기자신 포함시켜주고
                for lp in range(1,k+1): #범위 구하기
                    x1, y1=i+(dxx[0]*lp),j+(dyx[0]*lp)
                    x2, y2=i + (dxx[1] * lp),j + (dyx[1] * lp)
                    x3, y3=i+(dxx[2]*lp),j+(dyx[2]*lp)
                    x4, y4=i+(dxx[3]*lp),j+(dyx[3]*lp)
                    if dxx[0]!=0 and 0<=x1<n and 0<=y1<n and tree[x1][y1]!=-1 and tree[x1][y1]!=0:
                        #더이상 나아갈게 없지 않거나 격자 사이에 있고 비어있거나 벽이 아니어야됨
                        if(tree[x1][y1]>0):
                            sum_t+=tree[x1][y1] #해당나무 개수 더해주기
                    else:
                        dxx[0], dyx[0]=0,0
                    if dxx[1]!=0 and 0<= x2 < n and 0 <= y2 <n and tree[x2][y2] != -1 and tree[x2][y2] != 0:
                        if tree[x2][y2]>0:
                            sum_t += tree[x2][y2]
                    else:
                        dxx[1], dyx[1] = 0, 0
                    if dxx[2]!=0 and 0<=x3<n and 0<=y3<n and tree[x3][y3]!=-1 and tree[x3][y3]!=0:
                        if tree[x3][y3]>0:
                            sum_t+=tree[x3][y3]
                    else:
                        dxx[2], dyx[2]=0,0
                    if dxx[3]!=0 and 0<=x4<n and 0<=y4<n and tree[x4][y4]!=-1and tree[x4][y4]!=0:
                        if tree[x4][y4]>0:
                            sum_t+=tree[x4][y4]
                    else:
                        dxx[3], dyx[3]=0,0
                max_kill=max(max_kill, sum_t) #제일 큰 개수 넣어주고
                if temp!=max_kill: #제일 큰게 변경됐다면
                    kx,ky=i,j #좌표 저장
    return max_kill, kx, ky #킬수, 제초제 좌표


def kill_tree(kx, ky, year):
    dxx = [1, 1, -1, -1]
    dyx = [1, -1, 1, -1]
    tree[kx][ky]=year
    for lp in range(1, k + 1):  # 범위 구하기
        x1, y1=kx + (dxx[0] * lp), ky + (dyx[0] * lp)
        x2, y2=kx + (dxx[1] * lp),ky + (dyx[1] * lp)
        x3, y3=kx + (dxx[2] * lp),ky + (dyx[2] * lp)
        x4, y4=kx + (dxx[3] * lp),ky + (dyx[3] * lp)
        if dxx[0]!=0 and  x1< n and  y1< n and tree[x1][y1] != -1 :
            if tree[x1][y1] == 0:
                tree[x1][y1] = year
                dxx[0], dyx[0] = 0, 0
            else:
                tree[x1][y1] = year

        else:
            dxx[0], dyx[0] = 0, 0
        if dxx[1]!=0 and -1< x2< n and -1<y2<n and tree[x2][y2] != -1 :
            if tree[x2][y2] == 0:
                tree[x2][y2] = year
                dxx[1], dyx[1] = 0, 0
            else:
                tree[x2][y2] = year
        else:
            dxx[1], dyx[1] = 0, 0
        if dxx[2]!=0 and -1< x3<n and -1< y3< n and tree[x3][y3] != -1:
            if tree[x3][y3] == 0:
                tree[x3][y3] = year
                dxx[2], dyx[2] = 0, 0
            else:
                tree[x3][y3]= year

        else:
            dxx[2], dyx[2] = 0, 0
        if dxx[3] != 0 and -1 < x4 < n and -1 < y4 < n and tree[x4][y4] != -1:
            if tree[x4][y4] == 0:
                tree[x4][y4] = year
                dxx[3], dyx[3] = 0, 0
            else:
                tree[x4][y4] = year

        else:
            dxx[3], dyx[3] = 0, 0

for ing in range(3, m+3):
    visited = [[False for _ in range(n)] for _ in range(n)]
    tree_f, visited = growth(visited)
    expand(tree_f, visited)
    kk, kx, ky = find_kill()
    all_kill += kk

    kill_tree(kx, ky, (-1)*ing)
    if ing > 2+c:
        for i in range(n):
            for j in range(n):
                #print((ing-c)*(-1))
                if tree[i][j]==(ing-(c))*(-1):
                    tree[i][j]=0

print(all_kill)




