"""카탈란 수"""
dp=[0]*32
dp[0] = 1
dp[1] = 1
for i in range(2, 32):
    for j in range(1, i+1):
        dp[i] += dp[i-j] * dp[j-1]
while True:
    N = int(input())
    if N==0:
        break
    print(dp[N])

