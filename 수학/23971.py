h, w, n, m = map(int, input().split())
x,y = w//(m+1),h//(n+1)
if w%(m+1)!=0:
    x+=1
if h%(n+1)!=0:
    y+=1
print(x*y)

