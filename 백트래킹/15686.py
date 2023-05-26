import itertools
n, m = map(int, input().split())
streets = [list(map(int, input().split())) for _ in range(n)]

houses = []
chickens = []

def distance(c1, c2):
    x, y = c1
    a, b = c2
    return abs(x-a)+abs(y-b)

for i in range(n):
    for j in range(n):
        if streets[i][j] == 1:
            houses.append((i, j))
        elif streets[i][j] == 2:
            chickens.append((i, j))


temp=[]
chic_combi=[]
def dfs(start):

    if len(temp)==m:
        chic_combi.append(tuple(temp))
        return

    for i in range(start, len(chickens)):
        if chickens[i] in temp:
            continue
        temp.append(chickens[i])
        dfs(i)
        temp.pop()

dfs(0)

total_min_d = 100000
for c in chic_combi:
    total_d = 0
    for i in range(len(houses)):
        min_d = 10000
        for j in c:
            min_d = min(min_d, distance(houses[i], j))
        total_d+=min_d
    total_min_d = min(total_d, total_min_d)

print(total_min_d)