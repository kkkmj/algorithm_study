"""
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
"""

import itertools
n = int(input())

power = []
for _ in range(n):
    temp = list(map(int, input().split()))
    power.append(temp)

team = [i for i in range(n)]
com = itertools.combinations(team, n//2)

gap = 100
for loop in com:
    start = 0
    link = 0
    for i in loop:
        for j in loop:
            start+=power[i][j]
    for x in (set(team)-set(loop)):
        for y in (set(team)-set(loop)):
            link+=power[x][y]

    gap = min(gap, abs(start-link))
    if(gap==0):
        break

print(gap)


"""
많이 무식하게 풀었음
1. itertools 사용해서 조합 쓰기
2. 3중 반복문 돌리기
3. 2중 반복문 두번이나 쓰기
4. 같은 조합 안버리고 두번 쓰게 만들기
5. 조합이 하나 결정되면 다른것도 동시에 결정되는데 차집합 만들어서 집합 하나 더생기게 하기

솔직히 시간초과 날줄 알았는데 안나서 놀랐음 이게...파이썬?ㄷ

암튼 백트래킹 = dfs 랑 비슷한 의미를 갖고 있는 것 같음
그래서 보통 dfs로 푸는 것 같은데
dfs를 이용하면 굉장히 더 편하게 할 수 있는 듯 함.. 근데 왜지..?ㅎ;;

"""

# visited = [False]*n
# min_diff = 1000
#
# def Dfs(depth, idx):
#     global min_diff
#     if depth == n//2: #visited를 돌려서 팀을 다 나눴다면 합 구한 후 차 구하기
#         link, start = 0, 0
#         for i in range(n):
#             for j in range(n):
#                 if visited[i] and visited[j]:
#                     link += power[i][j]
#                 elif not visited[i] and visited[j]:
#                     start += power[i][j]
#         min_diff = min(min_diff, abs(link-start))
#         return #구했으니 나가줌
#     for i in range(idx, n): #팀이 n/2가 될때 까지 조합을 구해줌
#         #정확히 말해주면 idx는 인덱스 번호고 idx~n까지 돌아주는거라서 0부터의 조합부터 시작해서 쭉 돌려주는 것
#         if not visited[i]: #방문을 안했다면
#             visited[i] = True #하게 바꿔주고
#             Dfs(depth+1, i+1) #n/2될때 까지 재귀
#             visited[i] = False #이미 팀 짜쳤으니 False로 초기화
# Dfs(0,0)

"""백트래킹으로 풀면 다음과 같다

"""