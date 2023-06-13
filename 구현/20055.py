from collections import deque
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
belts = deque(map(int, input().split()))
robots=deque([-1]*(2*n))

i=1
level=0
while True:
    level+=1

    belts.rotate(1)
    robots.rotate(1)

    robots[n-1]=-1

    for j in range(n, 0, -1):
        if robots[j-1] != -1:
            if robots[j]==-1 and belts[j]>0:
                robots[j] = robots[j-1]
                robots[j-1] = -1
                belts[j]-=1

    robots[n-1]= -1

    if belts[0]!=0:
        robots[0]=i
        belts[0]-=1
        i+=1

    off=0
    for l in range(len(belts)):
        if belts[l]==0:
            off+=1

    if off >= k:
        break

print(level)