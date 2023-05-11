from collections import deque
import sys
input=sys.stdin.readline

s = deque(input().rstrip())
m = int(input())
temp_que=deque()

for _ in range(m):
    command = input().rstrip().split()
    if command[0]=='L':
        if s:
            temp_que.appendleft(s.pop())

    if command[0]=='D':
        if temp_que:
            s.append(temp_que.popleft())

    if command[0]=='B':
        if s:
            s.pop()

    if command[0]=='P':
        s.append(command[1])


print(''.join(s)+''.join(temp_que))


"""
긴 문자열은, 아니 그냥 문자열을 다룰때는 문자열로 다루면 안되고, stack과 que를 이용해서 다뤄야함.
아니면 시간초과가 남
이유?> 슬라이싱, """