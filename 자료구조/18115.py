from collections import deque

n = int(input())
skills = deque(map(int, input().split()))

floor = deque(i for i in range(n, 0, -1))
cards = deque()

while skills:
    skill = skills.pop()
    if skill == 1:
        cards.appendleft(floor.pop())
    elif skill == 2:
        # temp = cards.popleft()
        # cards.appendleft(floor.pop())
        # cards.appendleft(temp)
        #cards.insert(1, floor.pop())
        cards.rotate(-1)
        cards.appendleft(floor.pop())
        cards.rotate(1)
    elif skill == 3:
        cards.append(floor.pop())


print(* cards)

"""
굳이 rotate안하고 insert로도 해줄 수 있군..... 근데 음 rotate의 시간복잡도나 insert나 비슷하긴 할듯? 아닌가
rotate가 사실 pop하고 append나 다름 없는건데 시간복잡도 자체는 
rotate=insert>pop+append ... 가 아닌가 해봐야겟다

rotate=pop+append>insert 네..? 헐... i가 1밖에 안돼서 그런가 ㄹㅇ개의외다

그리고 그냥 1,2를 append하고 3을 appendleft하면
2번에서 insert시에 1이 아니라 -1에 insert가 가능해서 시간을 더 줄일 수 있음
그런다음 마지막엔 reverse로 해서 출력해주면됨
"""
