N = int(input())
road = list(input())

dp=[1e9]*N
dp[0]=0

for i in range(1, N):
    for j in range(i):
        if road[i]=="B" and road[j]=="J":
            dp[i] = min(dp[i], dp[j]+(i-j)**2)
        elif road[i]=="O" and road[j]=="B":
            dp[i] = min(dp[i], dp[j]+(i - j) ** 2)
        elif road[i]=="J" and road[j]=="O":
            dp[i] = min(dp[i], dp[j]+(i - j) ** 2)
if dp[-1]==1e9:
    print(-1)
else:
    print(dp[-1])

