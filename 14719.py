H, W = map(int, input().split())
blocks = list(map(int, input().split()))

temp = [[]]

for i in range(W):
    temp[-1].append(blocks[i])
    if blocks[i]==H:
        temp.append([])
        temp[-1].append(blocks[i])

left, right = 0, 0
for i in range(W):
    if left != 0 and right == 0:
    if left == 0:
        if blocks[i] != 0:
            left = blocks[i]





print(temp)