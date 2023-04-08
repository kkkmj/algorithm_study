"""그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다."""

from collections import deque

n, m, v= map(int, input().split())
graph=[[] for _ in range(n+1)]
visited=[False for _ in range(n+1)]

def dfs(node):
    visited[node]=True
    print(node, end=' ')

    for i in graph[node]:
        if visited[i]!=True:
            dfs(i)
def bfs(node):
    que= deque()
    visited[node]=True
    que.append(node)

    while que:
        k=que.popleft()
        print(k, end=' ')
        for p in graph[k]:
            if visited[p] == False:
                visited[p]=True
                que.append(p)

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(n+1):
    graph[i].sort()

dfs(v)
print()
visited=[False for _ in range(n+1)]

bfs(v)

"""
번호순으로 정렬 부분에서 
그래프의 개수가 n개가 아닌 0이 없어서 n+1인점을 망각해서 틀렸었음"""
