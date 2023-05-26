#TODO DP

n = int(input())
sceh=[list(map(int, input().split())) for _ in range(n)]
dp = [0]*(n+1)


for i in range(n-1, -1, -1):
    if i + sceh[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], sceh[i][1] + dp[i + sceh[i][0]])

print(max(dp))


# for i in range(n):
#     for j in range(i+sceh[i][0], n+1):
#         if dp[j] < dp[i] + sceh[i][1]:
#             dp[j] = dp[i] + sceh[i][1]

