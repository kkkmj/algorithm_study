import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
answer=[]
visited=[False]*n
check=[]
def dfs():
    if len(answer)==m:
        check.append(tuple(answer))
        return


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(li[i])
            dfs()
            visited[i]=False
            answer.pop()
dfs()
check = list(set(check))
check.sort()

for i in check:
    print(*i)
