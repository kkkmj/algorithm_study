n = int(input())
schedules = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if schedules[i][0] + i < n+1:
        dp[i] = max(dp[i + 1], dp[i+schedules[i][0]] + schedules[i][1])
    else:
        dp[i]=dp[i+1]

print(dp[0])

"""
나는 쓰레기야... dp 넘모 어렵다..ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
"""