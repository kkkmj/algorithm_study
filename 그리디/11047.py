N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

coin.sort(reverse=True)
cnt = 0
for c in coin:
    if K==0:
        break
    if c<=K:
        cnt += K//c
        K %= c
print(cnt)