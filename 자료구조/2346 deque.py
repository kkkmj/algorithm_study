from collections import deque

n = int(input())
balloons = deque(enumerate(map(int, input().split())))
answer = []
d=1

while balloons:
    b, i = balloons.popleft()
    answer.append(b+1)

    if i < 0:
        i = -i
    else:
        i = -(i-1)
    balloons.rotate(i)

print(* answer)

"""
나는... 빡대가리야....
라기 보다 일단 
1. rotate의 존재를 몰랐으며
2. 풍선에 tuple느낌으로 번호를 달 생각을 모댓음..ㅋ;;

둘다 핵심인데 그 둘을 다 몰랐으니..ㅎㅎ;;;  일단 2번같이 enumerate써서 해주는 생각은 정말 필요할듯!

그리고 0보다 클 때는 -=1 을 해주는 것도 포인트임
"""