dx, dy= [1, -1, 0, 0], [0, 0, 1, -1]

n=int(input())
cube=[]

answer=[]
for _ in range(n):
    cube.append(list(map(int, input())))


def dfs(node,c):
    x,y=node
    cube[x][y]=0
    for k in range(4):
        dxx, dyy=x+dx[k], y+dy[k]
        if -1<dxx<n and -1<dyy<n and cube[dxx][dyy]:
            c=dfs((dxx,dyy),c+1)
    return c
for i in range(n):
    for j in range(n):
        if cube[i][j]==1:
            answer.append(dfs((i,j),1))


answer.sort()
print(len(answer))
for a in answer:
    print(a)

"""
보통 이런 합 문제가 나올때는 dfs로 +1을 해가며 총 개수를 구하는게 가장 바람직한? 방법인 것 같다 왜냐면 굳이 계속 배열에 접근해서 값을 수정할 필요도 없고
재귀함수의 수만큼 구해서 해주는게 얼마나 멋잇는가! ㅋㅋ 장난이고 암튼 이런문제 풀때마다 이런식으로 해야지! 를 생각하지만 자꾸 까먹는지 뭔지 안하게 되는 것 같다
문제좀 많이 풀어서 해결방법을 잘 익히는게 필요할 듯
생각 못했던 점은
1. visited라는 배열을 쓸 필요 없이 방문했던 곳을 0 처리 시키는 것
2. 총 개수를 return해줄 때 어쨌든 한번의 함수에서 나온c를 리턴해주는 것이기 때문에 c=dfs() 이런식으로 해야지 총 개수를 구할 수 있다는 점
이정도가 있을 것 같다. 갔다온 곳은 0 처리 해주고, 간 만큼 +1 해주면서 dfs를 쓰는 방법! 꼭 생각하자!
"""