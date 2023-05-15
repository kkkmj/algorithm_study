import sys
input = sys.stdin.readline

n, m = map(int, input().split())
office_rooms = [input().strip() for _ in range(n)]
office_rooms.sort()
room_infos=[[i for i in range(9, 18)] for _ in range(n)]
for _ in range(m):
    room, s, t = map(str, input().strip().split())
    i=office_rooms.index(room)
    for t in range(int(s),int(t)):
        room_infos[i].remove(t)

for i in range(n):
    if not room_infos[i]:
        continue
    total_time=len(room_infos[i])
    if total_time==9:
        room_infos[i].clear()
        room_infos[i].append('09-18')
        continue
    if total_time==1:
        s = room_infos[i].pop()
        room_infos[i].append(str(s).zfill(2)+'-'+str(s+1).zfill(2))
        continue

    timeline=[]
    timeline[:]=room_infos[i][:]
    room_infos[i].clear()
    s=timeline[0]
    j=1
    while j!=total_time:
        if timeline[j]-timeline[j-1]!=1:
            room_infos[i].append(str(s).zfill(2)+'-'+str(timeline[j-1]+1).zfill(2))
            s=timeline[j]
        j+=1
    room_infos[i].append(str(s).zfill(2)+'-'+str(timeline[total_time-1]+1).zfill(2))

for i in range(n):
    print(f"Room {office_rooms[i]}:")
    if not room_infos[i]:
        print("Not available")
    else:
        print(f"{len(room_infos[i])} available:")
        for time in (room_infos[i]):
            print(time)
    if i!=n-1:
        print("-----")


"""
회의실 사용 가능 시간을 구할때 너무 하드코딩이라 마음에 들지 않음
찾은 방법으로는
1. 딕셔너리로 변환, 값은 [0]*18 로 배열을 만들어서 회의 시간 받을때 start, end까지 1로 설정
2. room=sorted(rooms.items()) 로 정렬+리스트화 시켜줌(아마 .items로 인해 리스트화가 되는듯)
3. 그리고 for문을 돌려서 temp리스트를 만들어 그전까지 1이고 값이0이 나왔다면 startTime, 그전까지 0이고 값이 1이 나왔다면 endTime
으로 해서 temp리스트에 리스트로 추가시켜줌
그리고 바로 밑에 print문을 돌려서 하나씩 추가.
for문안에 for문돌려서 구하는게 더 낫나? 싶었는데 그래도 나쁘진 않은 것 같음. 어쨌든 for문 이중으로 몇번 돌리는거나
한방에 처리할 수 있는 for문을 굳이 몇번 더 하는것 보다는 한방에 처리하는게 더 좋은듯
"""