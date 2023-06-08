from collections import deque
n, k = map(int, input().split())

visited=[-1]*100001


que = deque()
que.append(n)
visited[n]=0
while que:
    temp = que.popleft()

    if temp==k:
        break
    if temp<0:
        break
    if 0<2*temp<100001 and visited[2*temp]==-1:
        que.appendleft(2*temp)
        visited[2*temp]=visited[temp]
    if 0<=temp+1<100001 and visited[temp+1]==-1:
        que.append(temp+1)
        visited[temp+1]=visited[temp]+1
    if 0<=temp-1<100001 and visited[temp-1]==-1:
        que.append(temp-1)
        visited[temp-1]=visited[temp]+1

print(visited[k])

"""
0-1 bfs로 푸는 문제
그냥 뭐야 다른 BFS처럼 visited와 해결값을 동시에 쓰면 됨
"""