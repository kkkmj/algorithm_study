from collections import deque

t = int(input())
for _ in range(t):
    comand = input()
    n = int(input())
    if n==0:
        input()
        nums=deque()
    else:
        nums = deque(input()[1:-1].split(','))

    r_flag=0
    flag = 1
    for c in comand:
        if c == "R":
            r_flag+=1
        else:
            if nums:
                if r_flag%2==0:
                    nums.popleft()
                else:
                    nums.pop()
            else:
                flag = 0
                break
    if flag:
        print("["+",".join(nums)+"]")
        # ps = ""
        # if r_flag%2==0:
        #     while nums:
        #         if len(nums)==1:
        #             ps+=str(nums.pop())
        #         else:
        #             ps+=(str(nums.popleft())+',')
        # else:
        #     while nums:
        #         if len(nums)==1:
        #             ps+=str(nums.pop())
        #         else:
        #             ps+=(str(nums.pop())+',')
        #
        # print("["+ps+"]")
    else:
        print("error")

"""
와...쒸 천잰가
그냥 단순히 코딩을 하려고 하지말고
어떻게 해야 최적화할 수 있을까 생!각! 을 해보자
우선 for문을 여러번 돌리는 것 자체가 매우 시간이 많이 걸리는거라 
최소화 해야함!
문자열을 몇번 바꾸냐에 따라서 pop, popleft를 하는 식으로 그대로 냅둔다음에 마지막에 처리하면 되기 때문에
이런식으로 단순히 구현! 에 그치지 말고 좀 어떻게 해야 효율적일지 생각! 을 하자!
"""

"""
와 +로 여기서 어떻게 더 하냐면
r flag가 얼마나인지에 따라서 front와 back을 한 다음 문자열 인덱싱을 해줘서
[2:-3] 이런식으로도 가능함.... 문자열을 다룰때는 이런식으로 인덱싱 해주는게 굉장히 효율적으로 좋을듯
심지어 이러면 deque도 안쓰고 나중에 print문에서 깔끔하게 해줄 수 있음ㄷㄷ

+로 deque 아니더라도 어차피 여기서 숫자는 int가 아니어도 되기 때문에 int 처리 안해주고 첨부터 str 처리로 해주면 deque제외하고도 그냥
''.join(deque) 이렇게도 가능함!
"""