N, K = map(int, input().split())
bag = [list(map(int, input().split())) for _ in range(N)]

dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j<bag[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-bag[i-1][0]]+bag[i-1][1])
print(dp[-1][-1])