n, m = map(int, input().split())
li=list(map(int, input().split()))
li.sort()
answer=[]
visited=[False]*n
check=[]
def dfs():

    if len(answer)==m:
        if answer not in check:
            check.append(answer[:])
            print(' '.join(map(str, answer)))
        return


    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(li[i])
            dfs()
            visited[i]=False
            answer.pop()
dfs()

