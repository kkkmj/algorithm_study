import sys
input = sys.stdin.readline
n, l = map(int, input().split())
point = list(map(int,input().split()))
point.sort()
k=l-1
answer=1
for i in range(1,n):
    if point[i]-point[i-1]<=k:
        k-=point[i]-point[i-1]

    else:
        k=l-1
        answer+=1

print(answer)