n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()
answer=[]

def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start,n):
        answer.append(li[i])
        dfs(i)
        answer.pop()

dfs(0)