cards = [i for i in range(1, 35)]
num = list(input())
l = len(num)
answer = 1

dp = [0]*l

for i in range(l-1):
    if int(num[i]+num[i+1]) in cards:
        dp[i]=dp[i-1]+1

