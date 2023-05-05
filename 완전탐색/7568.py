import sys

input = sys.stdin.readline
n = int(input())
info = []
rank = [1] * n
for _ in range(n):
    x, y = map(int, input().split())
    info.append((x, y))

for i in range(n):
    for j in range(n):
        x, y = info[i]
        a, b = info[j]
        if x < a and y < b:
            rank[i] += 1
print(*rank)

