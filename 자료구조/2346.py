from collections import deque
n = int(input())
nums = list(map(int, input().split()))
#balloons=deque(1 for _ in range(n-1))
balloons = [1]*n

d=1
answer=[1]
i=0
k=nums[0]
if k<0:
    d=-1
balloons[0]=0

for _ in range(n-1):
    l = n-len(answer)

    while k!=0:
        i=i+1*d
        if i > n-1:
            i=0
        if i < 0:
            i = n-1

        if balloons[i]!=0:
            k=k-(1*d)
    if nums[i]>0:
        d=1
    else:
        d=-1

    balloons[i] = 0
    answer.append(i + 1)

    if abs(k)>l:
        k = ((nums[i] * d) % l) * d
    else:
        k = nums[i]


print(*answer)

