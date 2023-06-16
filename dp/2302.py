n = int(input())
m = int(input())
vips = [int(input()) for _ in range(m)]

dp=[1, 1, 2]

for i in range(3, 41):
    dp.append(dp[i-1]+dp[i-2])

answer = 1
if m>0:
    pre = 0
    for i in range(m):
        answer = answer * dp[vips[i]-1-pre]
        pre = vips[i]
    answer = answer*dp[n-pre]
else:
    answer = dp[n]

print(answer)

"""
# 처음 접근했던 방식
n = int(input())
m = int(input())
# vips = [int(input()) for _ in range(m)]
vips = [False] * (n+1)
for _ in range(m):
    vips[int(input())] = True

dp=[1, 1]

for i in range(3, n+1):
    if vips[i] or vips[i-1]:
        dp.append(dp[i-1])
    else:
        if vips[i-2]:
            dp.append(dp[i-1]*2)
        else:
            dp.append(dp[i-1]+dp[i-2])
print(dp[-1])
"""

"""
어렵다 어려워..ㅠ
나는 역시 함수로 dp하는 것 보다는 수열 나열한다음 규칙 찾아서 점화식 나열하는게 훨 편하다..
"""