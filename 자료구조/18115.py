from collections import deque

n = int(input())
skills = deque(map(int, input().split()))

floor = deque(i+1 for i in range(n))
cards = deque()

for skill in skills:
    if skill == 1:
        cards.appendleft(floor.popleft())
    elif skill == 2:
        if len(floor)>1:
            temp = floor.popleft()
            cards.appendleft(floor.popleft())
            floor.appendleft(temp)
    elif skill == 3:
        if len(floor) > 1:
            cards.appendleft(floor.pop())


answer=[0]*n

for i in range(n):
    answer[cards[i]-1]=i+1

print(* answer)
