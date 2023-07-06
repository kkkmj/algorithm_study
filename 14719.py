H, W = map(int, input().split())
blocks = list(map(int, input().split()))

temp = [[]]

for i in range(W):
    temp[-1].append(blocks[i])
    if blocks[i]==H:
        temp.append([])
        temp[-1].append(blocks[i])




print(temp)