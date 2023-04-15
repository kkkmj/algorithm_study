n, m = map(int, input().split())
answer=[]
li=list(map(int, input().split()))

li.sort()



def dfs(start):
    if len(answer)==m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, len(li)):
        if li[i] not in answer:
            answer.append(li[i])
            dfs(i)
            answer.pop()

dfs(0)

"""당연하게 생각하지 말자
알고있다고 생각하지 말자
처음부터 다시 생각하자"""