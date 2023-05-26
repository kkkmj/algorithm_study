T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    coords=[0]*10001
    answer=0
    for _ in range(n):
        i, f = map(int, input().split())
        coords[i]=f
    #coords = [list(map(int, input().split())) for _ in range(n)] #좌표, 강도
    i=1
    while i<10001:
        #print(i)
        if coords[i]!=0:
            force=coords[i]
            i+=(force+1)
            answer+=1
            if i > 10000:
                break
        else:
            i+=1


    print(f"#{test_case} {answer}")
