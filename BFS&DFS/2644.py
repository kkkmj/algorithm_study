
n = int(input())
con = [[] for _ in range(n+1)]
visited = [False]*(n+1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    con[x].append(y)
    con[y].append(x)

def dfs(node, answer):
    if node==b:
        print(answer)
        exit(0)

    if visited[node]:
        print(-1)
        exit(0)
    visited[node]=True
    for i in con[node]:
        if not visited[i]:
            answer+=1
            dfs(i, answer)
            answer-=1

    return -1

print(dfs(a,0))

"""
dfs를 자꾸 visited로 False, True 하는 경향이 있는데
그냥 0으로 초기화 시키고 거기에 접근한 만큼 +1 해주는 방법도 있음
"""