N = int(input())

# for _ in range(N):
#     R, G, B = map(int, input().split())

house = [(list(map(int,input().split()))) for _ in range(N)]
house.reverse()
"""
대충 흠... 그 전이랑 색이 달라야됨.
값은 최소
근데 그건있음. 
"""
r, g, b = [0]*(N), [0]*(N), [0]*(N)
r[0], g[0], b[0] = house[0]

for i in range(1, N):
    r[i] = min(g[i-1], b[i-1]) + house[i][0]
    g[i] = min(r[i-1], b[i-1]) + house[i][1]
    b[i] = min(r[i-1], g[i-1]) + house[i][2]


print(min(r[-1], g[-1], b[-1]))

"""
이거 심지어 굳이 메모리 쓸 필요 없이 그냥 최신값 계속 갱신하면서 해줄 수 있음

예를 들어

"""
for i in range(1, N):
    house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
    house[i][1] = min(house[i - 1][0], house[i - 1][2]) + house[i][1]
    house[i][2] = min(house[i - 1][0], house[i - 1][1]) + house[i][2]

"""
이렇게 하면 그 전 값 계속 갱신하면서 별다른 메모리값 소모 없이 만들어 줄 수 있음.
"""

"""
넘모 어렵다..ㅠㅠ
"""