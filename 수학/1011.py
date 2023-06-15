T = int(input())

dp = [0]*50000
dp[0]=0
# for i in range(1, 50000):
#     dp[i] = dp[i - 1] + i * 2
# print(dp[-1])

for _ in range(T):
    x, y = map(int, input().split())
    d = y-x
    if d==1:
        print(1)
        continue

    answer = 0
    step = 0
    temp = 0
    for i in range(1, d):
        if dp[i]!=0:
            if dp[i]>d:
                temp = dp[i-1]
                step = i-1
                break
            continue
        dp[i] = dp[i - 1] + i * 2
        if dp[i] > d:
            temp = dp[i - 1]
            step = i-1
            break


    answer = step*2
    d -= temp
    if d==0:
        pass
    elif d<=step+1:
        answer+=1
    else:
        #answer+=d//step
        answer+=2
    # if d%step

    print(answer)

