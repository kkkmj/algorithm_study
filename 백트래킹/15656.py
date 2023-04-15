n, m = map(int, input().split())

li = list(map(int, input().split()))
li.sort()
answer=[]

def dfs():
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return

    for i in range(n):
        answer.append(li[i])
        dfs()
        answer.pop()

dfs()