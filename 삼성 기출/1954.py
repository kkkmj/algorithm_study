t = int(input())
for i in range(1, t+1):
    num = int(input())
    matrix=[[0 for _ in range(num)] for _ in range(num)]
    x, y = 0,0
    matrix[x][y]=1
    po=[(0,1)]
    n=num

    for k in range(2, n*n+1):
        dx, dy = po[0]
        nx=x+dx
        ny=y+dy
        if nx==n or ny==n:
            if nx==n:
                nx-=1
            else:
                ny-=1
        if(nx==num-n and dy==1):
            x=nx
            y=ny
        elif y==n-1 and dy==1:
            po[0]=(1,0)
            x+=1
        elif y==n-1 and dx==1:
            x=nx
            y=ny
        elif x==n-1 and dx==1:
            po[0]=(0, -1)
            y-=1
        elif x==n-1 and dy==-1:
            x=nx
            y=ny
        elif y==n-num and dy==-1:
            po[0]=(-1,0)
            n-=1
            x-=1
        elif y==n-num and dx==-1:
            x = nx
            y = ny
        elif y==n-num and dx==-1:
            po[0]=(0,1)
            y+=1
        matrix[x][y]=k

    #
    # for k in range(2, n*n+1):
    #     if x==n or y==n:
    #         if x==n:
    #             x-=1
    #         else:
    #             y-=1
    #     if (x==n-1):
    #         if y==n-1:
    #             y -= 1
    #         elif y==num-n:
    #             n = n - 1
    #             x -= 1
    #         else:
    #             y-=1
    #
    #     elif y==num-n:
    #         # if x==num-n:
    #         #     y+=1
    #         # else:
    #             x-=1
    #     elif x==n-1:
    #         y-=1
    #     elif y==n-1 and x==n-1:
    #         y-=1
    #     elif (y==n-1):
    #         # if x==n-1:
    #         #     y-=1
    #         # else:
    #             x += 1
    #     elif x==num-n and y==n-1:
    #         x+=1
    #     elif x==num-n:
    #         # if y!=num-n:
    #         #     x-=1
    #         # else:
    #             y+=1

        matrix[x][y]=k




    print('#'+str(i))
    print(matrix)

