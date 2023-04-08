from collections import deque
n = int(input()) #n은 반드시 홀수 3<=n<=29
figure = []

to_art_score=0
for _ in range(n):
    figure.append(list(map(int, input().split()))) #1<=?<=10

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(visited, node, fig_num, g_num): #visited=방문정보, node, 조사할 위치좌표, figure숫자 정보, 그룹 num번호
    cnt=0 #현재 조사하고 있는 거의 개수
    que = deque()
    x,y=node
    visited[x][y]=True
    group[x][y]=g_num
    que.append(node)

    while que:
        x, y = que.popleft()
        cnt += 1  # 개수 올림
        for i in range(4):
            dxx=x+dx[i]
            dyy=y+dy[i]
            if -1<dxx<n and -1<dyy<n and visited[dxx][dyy]==False: #만약 조건이 성립된다면
                now = figure[dxx][dyy]  # 상하좌우 했을때의 fig숫자
                if fig_num==now: #상하좌우의 위치가 fig숫자 정보와 일치하면
                    que.append((dxx,dyy))
                    visited[dxx][dyy]=True
                    group[dxx][dyy]=g_num #그룹 지도에 정보 반영

    return cnt

def bfs2(node, graph):
    que = deque()
    que.append(node)

    while que:
        x, y = que.popleft()
        g_num=group[x][y]
        for i in range(4):
            dxx=x+dx[i]
            dyy=y+dy[i]
            if -1<dxx<n and -1<dyy<n: #만약 조건이 성립된다면
                now = group[dxx][dyy]  # 상하좌우 했을때의 fig숫자
                if now!=g_num: #숫자정보가 다르면
                    if now in graph[g_num]: #만약 인접 정보가 이미 저장되어 있다면
                        graph[g_num][now]+=1 #인접한면 +1
                    else: #인접정보가 없다면
                        graph[g_num][now]=1 #인접정보 갱신


def make_score(visit, node, graph, g_combi):
    score=0
    que=deque()
    que.append(node)
    visit[node]=True

    while que:
        g_num=que.popleft()
        for i in graph[g_num]:
            if not visit[i]:

                f_num, cnt1=g_combi[g_num]
                f_num2, cnt2 = g_combi[i]
                score+=(cnt1+cnt2)*f_num*f_num2*graph[g_num][i]
    return score



def rotate():
    c=n//2

    for i in range(1,c+1):
        temp=figure[c][c-i]
        figure[c][c-i]=figure[c][c+i]
        figure[c][c + i]=figure[c+i][c]
        figure[c+i][c ]=temp

        # new_fig[c+i][c ]=figure[c][c-i]
        # new_fig[c][c-i]=figure[c][c+i]
        # new_fig[c][c + i]=figure[c+i][c]
        # new_fig[c+i][c ]=figure[c][c-i]


    for i in range(1, c+1):
        figure[c+1][c+i+1]=figure[c+1][c+1]


십자 모양을 제외한 4개의 정사각형은 각각 개별적으로 시계 방향으로 90'씩 회전이 진행됩니다.



for _ in range(4):

    group = [[-1 for _ in range(n)] for _ in range(n)]
    group_num = -1 #그룹 개수
    g_combi = [] #조화에 필요한 정보
    score_li=[]
    graph=[] #인접 정보
    visited = [[False for _ in range(n)] for _ in range(n)]


    for i in range(n):
        for j in range(n):
            if not visited[i][j]:#이차원 배열 돌면서 방문한적이 없다면
                graph.append({})  # 인접 정보 저장할 그래프 생성
                group_num += 1 #그룹 개수 +1
                fig_num = figure[i][j] #그룹의 숫자값
                cnt = bfs(visited, (i, j), fig_num, group_num)
                g_combi.append((fig_num, cnt)) #그룹 숫자값, 개수 추가
    for i in range(n):
        for j in range(n):
            bfs2((i,j), graph)

    g_visit = [False]*(group_num+1)
    for i in range(group_num):
        score_li.append(make_score(g_visit, i, graph, g_combi))






    #to_art_score+=



#print(to_art_score)