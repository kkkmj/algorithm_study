N = int(input())
dp=[1, 3]

for i in range(2, N+1):
    dp.append((dp[i-1]*2 + dp[i-2])%9901)

print(dp)

"""
dp넘모 어렵고...ㅠ
"""