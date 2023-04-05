data=list(input())
rod = 0
con = 0
answer = 0
for i in range(1, len(data)+1):
    if(data[i]!=data[i-1]):
        if(rod==0):
            rod+=1
            con+=1
        else:
            answer+=rod*2

    else:
        rod+=1

