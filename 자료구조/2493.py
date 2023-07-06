import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
sos = []
answer = []
for i in range(N):
    while sos:
        if sos[-1][1] > tops[i]:
            answer.append(sos[-1][0]+1)
            break
        else:
            sos.pop()
    if not sos:
        answer.append(0)
    sos.append((i, tops[i]))

print(*answer)

"""
어룝다 어려워
결론적으로 이거는 맨 오르ㅜㄴ쪽ㅇ서 pop해서 접근할게 아니라
왼쪽부터 순차적으로 접근한 다음
큰값 저장하고 큰값이 아니면 pop하면서 해야되는 묹로군...ㅠㅠ
"""