n, m = map(int, input().split())
li = list(map(int, input().split()))
answer=[]
li.sort()

def dfs():
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in li:
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()

dfs()