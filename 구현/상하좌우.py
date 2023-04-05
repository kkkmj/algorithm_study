x=0
y=0

n = int(input())
road = list(input().split())

for dir in road:
    if(dir == "R"):
        y += 1
        if(y>n-1):
            y-=1
    elif(dir == "L"):
        y -= 1
        if(y<0):
            y+=1
    elif dir == "U":
        x -=1
        if x<0:
            x+=1
    elif dir == "D":
        x += 1
        if x>n-1:
            x-=1


print(x+1, y+1)
# x, y = 1, 1
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# for plan in road:
#     for i in range(len(move_types)):
#         if plan == move_types[i]:
#             nx = x+dx[i]
#             ny = y +dy[i]
#     if nx<1 or ny<1 or nx>n or ny >n:
#         continue
#     x, y = nx, ny
#
# print(x, y)