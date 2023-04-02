"""신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.



어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오."""
#TODO DFS
def dfs(graph, start, check):
    check[start]=True
    for i in graph[start]:
        if not check[i]:
            dfs(graph, i, check)




n = int(input())
com = [False]*(n+1)
net = [[] for i in range(n+1)]
c = int(input())
for i in range(c):
    com1, com2 = map(int, input().split())
    net[com1].append(com2)
    net[com2].append(com1)

dfs(net, 1, com)

print(sum(com)-1)

"""
사실 bfs나 dfs나 상관없긴 한데 굳이 bfs로 풀필요가 없어서 dfs로 풀었음
2차원배열 초기화 하는 방법은
[[] for _ in range(n+1)] 이런식으로 하면 2차원 배열을 초기화시켜줄 수 있음!

그리고 dfs에서 굳이 인자로 graph와 visited를 왜 받아야되는지는 생각해봐야할 문제인것 같다. 
왜냐면 어차피 파일 내에 같은 변수들이라서 
다른건 모르겠는데 start부분은 계속 바뀌는거고, 암튼 현재 위치를 쭉 찾아나가는거 말고 필요 없으니
이렇게 해주면 될듯..?
"""
