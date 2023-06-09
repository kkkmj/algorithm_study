n, s, r = map(int, input().split())
team = [0]*(n+2)
broken = list(map(int, input().split()))
more = list(map(int, input().split()))

for i in range(s):
    team[broken[i]]+=-1

for i in range(r):
    team[more[i]]+=1

broken.sort()

for i in range(s):
    b = broken[i]
    if team[b]==0:
        continue
    elif team[b-1]==1:
        team[b-1]=0
        team[b]=0
    elif team[b+1]==1:
        team[b + 1] = 0
        team[b] = 0

sum = 0
for i in range(n+2):
    if team[i]==-1:
        sum+=1

print(sum)

"""
별거 아닌걸로 너무 헤맸다... ...
내가 정한 인덱스를 제대로 확인해서 해주자...
n만큼 팀을 만든게 아니라 n+2만큼 팀을 만들어줬으면 그만큼 돌려야지!

그리고 오히려 입력이나 그런값들이 적을 수록 remove가 그렇게 느리지 않음
"""