import sys
input=sys.stdin.readline

n, m = map(int, input().split())
nums=list(map(int, input().split()))
num_sum=[0]*n
num_sum[0]=nums[0]
for i in range(1,n):
    num_sum[i]=nums[i]+num_sum[i-1]

for _ in range(m):
    i, j = map(int, input().split())
    if i==1:
        print(num_sum[j-1])
    else:
        print(num_sum[j-1]-num_sum[i-2])