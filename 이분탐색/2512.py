N = int(input())
res = list(map(int, input().split()))
M = int(input())

res.sort()
money = M//N

for i in range(N):
    if money >= res[i]:
        M -= res[i]
    else:
        money = M//(N-i)
        if money>=res[i]:
            M-= res[i]
        else:
            break

if res[-1]<money:
    print(res[-1])
else:
    print(money)
