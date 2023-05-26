from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]

def bfs(node):
    a,b = node
    times[a][b]=0
    que = deque()
    que.append(node)

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if -1 < nx < n and -1 < ny < n:
                if areas[nx][ny]+times[x][y] < times[nx][ny]:
                    que.append((nx, ny))
                    times[nx][ny] = areas[nx][ny]+times[x][y]

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    areas = [list(map(int, input())) for _ in range(n)]
    times = [[10000]*n for _ in range(n)]
    bfs((0, 0))
    print(f"#{test_case} {times[n-1][n-1]}")
