import heapq
N = int(input())

tables= []
for _ in range(N):
    table = (list(map(int, input().split())))
    for i in table:
        heapq.heappush(tables, i)

    if len(tables)>N*2:
        #tables = tables[N-1:]
        for _ in range(N-1):
            heapq.heappop(tables)

tables.sort()
print(tables[-N])