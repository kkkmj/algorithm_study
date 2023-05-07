import sys

input = sys.stdin.readline
n = int(input())
info=[]
answer=1
for _ in range(n):
    info.append(tuple(map(int, input().split())))
info.sort(key=lambda x:(x[1],x[0]))
last = info[0][1]
for i in range(1,n):
    if last<=info[i][0]:
        answer+=1
        last=info[i][1]


print(answer)

"""
결국 다른사람꺼 보고 했음
사실 아직도 왜 그런지 잘 모르겠다....
암튼 시작하는 시간부터 하면 경우의 수도 더 많아지고, 오히려 끝내는 시간이 늘어날 수도 있음
그렇기 때문에 끝나는 시간기준으로 정렬하고, 그다음엔 시작하는 시간으로 정렬한다면 끝나는 시간 기준으로만 계산할 수 있음
그래서 굳이 list에 저장해서 비교할게 아니라 last시간을 지정해준 다음 그 last시간보다 길다면 개수를 + 해주고 last를 다시 대입해줌
그래서 여기서 포인트는 그리드는 어차피 뭐 완벽하고, 정확하고 구체적인 답을 구하는게 아님.
이런게 진짜 그리디 문제 같긴한데
암튼 진짜 다른거 아니고 last하나만으로 판단하고, 저장하는 이유가 있음. 이런게 그리디임. 
"""