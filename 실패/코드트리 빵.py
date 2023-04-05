from collections import deque
n, m = map(int, input().split())
EMPTY = (-1, -1)
roads = [[] for _ in range(n)]
conv = []
for _ in range(n):
    roads.append(list(map(int, input().split())))
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    conv.append((x-1, y-1))

people = [EMPTY] * m
n_time = 0
"""위치의 핵심은
2차원 배열이 아닌
배열 안에 튜플(x,y) 값을 저장 하는 것! 이라기엔 튜플은 변경이 안되는데 어떻게 하려고 그러는거지..?"""

dxs = [-1, 0, 0, 1]
dys = [0, -1, 1, 0]

step = [[0] * n for _ in range(n)]

visited = [[False]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    return in_range(x, y) and not visited[x][y] and roads[x][y] != 2

def bfs(start_pos):
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
            step[i][j] = 0
    q = deque()
    q.append(start_pos)
    sx, sy = start_pos
    visited[sx][sy] = True
    step[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in  zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx, ny))



"""
 ↑, ←, →, ↓ 의 우선 순위
 
 1. 베캠 자리 찾기
 
 """