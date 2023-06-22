import sys
N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False]*(M+1) for _ in range(N)]


if S+V[0]<M+1:
    dp[0][S+V[0]]=True
if S-V[0]>-1:
    dp[0][S-V[0]] = True

for i in range(1, N):
    for j in range(M+1):
        if dp[i-1][j]:
            if j+V[i]<M+1:
                dp[i][j+V[i]]=True
            if j-V[i]>-1:
                dp[i][j-V[i]] = True

for i in range(M, -1, -1):
    if dp[N-1][i]:
        print(i)
        sys.exit(0)

print(-1)

"""
대체 이런생각을 어떻게 할 수 있는거지.....
쩌네...
"""