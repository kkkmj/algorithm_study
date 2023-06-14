import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trains = [0]*(n)

for _ in range(m):
    command = input()

    if command[0]=='1':
        c, i, x = map(int, command.split())
        trains[i-1] |= (1<<x)
        #trains[i-1] = trains[i-1] | (1 << x)
        # 즉 1<<x 해서 해당 비트 자리에 1띄운 값을 |  로 그 자릿수에 1추가되게 만듦

    elif command[0]=='2':
        c, i, x = map(int, command.split())
        trains[i-1] &= ~(1 << x)
        #trains[i-1] = trains[i-1] & ~(1<<x)
        #x가 3이면 ~때문에 0111이 되는거고(3을 0으로 만들고 나머진1로) &로 교집합이니까 나머지 교집합으로

    elif command[0] == '3':
        c, i = map(int, command.split())
        trains[i-1] <<= 1
        #trains[i-1] = trains[i-1] << 1 이건 ...엥 아 비트 옮기면 새로운 0은 추가되지만 맨 끝사람이 나가진 않음
        trains[i-1] &= ~( 1<< 21)
        #그래서 맨 끝사람 없애주기


    elif command[0] == '4':
        c, i = map(int, command.split())
        trains[i-1] >>= 1
        trains[i-1] &= ~1 # ~(1<<0) = ~1 과 똑같음. 그래서 ~1 만 해주면 됨.
        # #어..? 근데 생각해보니까 어차피 이건 이거 필요 없는디..? 오히려 잇으면 안될텐데 가 아니라 걍 0 자체를 생각 안한거군

print(len(set(trains)))