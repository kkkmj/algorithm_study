#누적합 구하기
n, m = map(int, input().split())
cars = [0]+list(map(int, input().split()))
total_car = [0]*(n+1)
#아마 100000
for i in range(1,n+1):
    total_car[i]=total_car[i-1]+cars[i]


for _ in range(m):
    s, t = map(int, input().split())

    total=total_car[t]-total_car[s-1]

    print(total)
