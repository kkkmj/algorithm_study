n = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

des = sum(roads)
total=prices[0]*roads[0]
min_p=prices[0]
for i in range(1,n-1):
    min_p = min(min_p, prices[i])
    total+=min_p*roads[i]

print(total)