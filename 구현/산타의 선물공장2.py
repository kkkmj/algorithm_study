"""더블 링크드 리스트 로 풀어야함...근데....이거 맞아..?ㅠ 테케는 다 맞음... 시간최적화(자료구조) 문제"""
from collections import deque

def install(n, m, boxes):
    belt = [deque([]) for _ in range(n)]
    for i in range(0, m):
        belt[boxes[i]-1].append(i+1)
    return belt

def all_shift(m_src, m_dst, belt):
    while belt[m_src-1]:
        belt[m_dst-1].appendleft(belt[m_src-1].pop())
    return len(belt[m_dst-1])

def front_shift(m_src, m_dst, belt):
    if not belt[m_src-1] and not belt[m_dst-1]:
        return 0
    elif not belt[m_src-1] and belt[m_dst-1]:
        belt[m_src-1].append(belt[m_dst-1].popleft())
    elif belt[m_src-1] and not belt[m_dst-1]:
        belt[m_dst - 1].append(belt[m_src - 1].popleft())
    elif belt[m_src - 1] and belt[m_dst - 1]:
        x = belt[m_src-1].popleft()
        y = belt[m_dst-1].popleft()
        belt[m_src-1].appendleft(y)
        belt[m_dst-1].appendleft(x)
    return len(belt[m_dst-1])

def div(m_src, m_dst, belt):
    n = len(belt[m_src-1])
    if n > 1:
        for _ in range(int(n/2)):
            belt[m_dst-1].appendleft(belt[m_src-1].popleft())
    return len(belt[m_dst-1])

def g_info(p_num, belt):
    a, b = -1, -1
    for i in range(len(belt)):
        for j in range(len(belt[i])):
            if belt[i][j] == p_num:
                if j>0:
                    a = belt[i][j-1]
                if j!=len(belt[i])-1:
                    b = belt[i][j+1]
    return (a + (2 * b))

def b_info(b_num, belt):
    a, b = -1, -1
    if belt[b_num-1]:
        a = belt[b_num-1][0]
        b = belt[b_num-1][-1]
    return (a + (2 * b) + (3 * (len(belt[b_num-1]))))


q = int(input())
init = list(map(int, input().split()))
init.pop(0)
belt = install(init.pop(0), init.pop(0), init)
for _ in range(q-1):
    func_info = list(map(int, input().split()))
    num = func_info.pop(0)
    if num == 200:
        print(all_shift(func_info.pop(0), func_info.pop(0),belt))
    elif num == 300:
        print(front_shift(func_info.pop(0),func_info.pop(0),belt))
    elif num == 400:
        print(div(func_info.pop(0), func_info.pop(0), belt))
    elif num == 500:
        print(g_info(func_info.pop(0), belt))
    elif num == 600:
        print(b_info(func_info.pop(0), belt))


