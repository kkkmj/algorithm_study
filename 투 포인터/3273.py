n = int(input())

nums = list(map(int, input().split()))
x = int(input())

nums.sort()
s = 0
e = n-1
ans = 0
while s<e:
    if nums[s]+ nums[e] == x:
        ans+=1
        s+=1
        e-=1
    elif nums[s] + nums[e] > x:
        e-=1
    else:
        s+=1

print(ans)

