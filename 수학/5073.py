while True:
    triangle=list(map(int, input().split()))
    triangle.sort()
    if not sum(triangle):
        break

    if triangle[0]+triangle[1]>triangle[2]:
        l = set(triangle)
        if len(l)==3:
            print("Scalene")
        elif len(l)==2:
            print("Isosceles")
        else:
            print("Equilateral")
    else:
        print("Invalid")