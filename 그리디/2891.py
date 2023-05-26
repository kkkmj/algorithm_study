n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
more = list(map(int, input().split()))
broken.sort()
more.sort()
answer=[]
while broken or more:
    b = broken.pop()
    m = more.pop()
    if b-2<m<b+2:
        pass
    elif b+1 < m:
        while b+1 < more[-1]:
            more.pop()
        if b-2<more[-1]<b+2:
            more.pop()
    else:
        more.append(m)
        answer.append(b)


print(len(answer))