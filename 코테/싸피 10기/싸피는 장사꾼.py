T = int(input())
for test_case in range(1, T + 1):
    car = False
    n = int(input())
    customers = [list(map(int, input().split())) for _ in range(n)] #1=팜, -1=삼
    # sell_cars=[0]*n
    # get_cars=[0]*n
    # for i in range(n):
    #     s, p = map(int, input().split())
    #     if s==1:
    #         get_cars[i] = p
    #     else:
    #         sell_cars[i] = p
    get_cars=[]
    sell_cars=[]
    now_money=0
    total=0

    for i in range(n):
        service, price = customers[i]
        if service==-1:
            if now_money<price:
                if not car and get_cars:
                    if price in get_cars:
                        total-=now_money
                        now_money=price
                        total+=price
                elif car and get_cars:
                    if price in get_cars:
                        car=False
                        total+=price
                        now_money=price
        else:
            car = True
            get_cars.append(price)

    print(f"#{test_case} {total}")
