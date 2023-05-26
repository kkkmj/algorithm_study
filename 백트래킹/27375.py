n, k = map(int, input().split())
#w 요일 1~5/ s, e = 1~10
lessons = [list(map(int, input().split())) for _ in range(n)]
lessons.sort(key = lambda x:(x[0], x[1], x[2]))
answer=[]
temp=[]
visited = [False]*n

def dfs(start, total):
    if total>k:
        return
    if total==k:
        answer.append(tuple(temp))
        return

    for i in range(start, n):
        if lessons[i][0]==5: #금요일이면 out
            continue

        if temp:
            if temp[-1][0] == lessons[i][0]:
                if temp[-1][2] >= lessons[i][1]: #전수업과 겹치면 out #여기도 굳이 이중if문 하지 말고 걍 붙여도 되니까 and로 해주기
                    continue
        credit = lessons[i][2]-lessons[i][1]+1

        if not visited[i]:
            temp.append(lessons[i])
            visited[i]=True
            dfs(i+1, total+credit)
            temp.pop()
            visited[i]=False

dfs(0, 0)
print(len(answer))


"""
결국 문제는 for문 안에 15가 안넘을 경우만 dfs굴린게 문제였는데...
이게 왜 문제인지는 잘 모르겠군

그리고 이렇게 개수만 구하는 식이면 굳이 temp로 append하는 식으로 하지 말고
total이 15가 되면 answer+=1 하는식으로 해주면 됨
"""