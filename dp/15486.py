import sys
input = sys.stdin.readline
n = int(input())
scehdule = [list(map(int, input().split())) for _ in range(n)]

dp = [0]*(n+1)

# scehdule.reverse()
# for i in range(1,n+1):
#     if scehdule[i-1][0] > i:
#         continue
#     dp[i] = max(dp[i], dp[i-scehdule[i-1][0]]+scehdule[i-1][1])

for i in range(n-1, -1, -1):
    if scehdule[i][0] <= n-i:
        dp[i] = max(dp[i+1], dp[i+scehdule[i][0]]+scehdule[i][1])
    else:
        dp[i]=dp[i+1]

print(dp[0])

#reverse 하면 시간초과남