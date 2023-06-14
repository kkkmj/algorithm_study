n, m = map(int, input().split())
trains = [[False]*20 for _ in range(n)]
commands = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    command = commands[i][0]
    if command==1:
        trains[commands[i][1]-1][commands[i][2]-1]=True
    elif command==2:
        trains[commands[i][1]-1][commands[i][2]-1]=False
    elif command == 3:
        trains[commands[i][1]-1].pop()
        trains[commands[i][1]-1].insert(0, False)

    elif command == 4:
        del trains[commands[i][1]-1][0]
        trains[commands[i][1]-1].append(False)

for i in range(n):
    trains[i]=tuple(trains[i])

print(len(set(trains)))