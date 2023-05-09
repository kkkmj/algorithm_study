import sys
input = sys.stdin.readline
s = input().strip()
bomb_s = list(input().strip())
n=len(bomb_s)
new_string=[]
new_string[:]=s[:n-1]

for c in range(n-1,len(s)):
    if s[c]==bomb_s[-1]:
        if new_string[-n+1:]==bomb_s[:-1]:
            for _ in range(n-1):
                new_string.pop()
        elif n!=1:
            new_string.append(s[c])
    else:
        new_string.append(s[c])
"""
이부분은 우선 .append를 해준 다음, if로 처리해주는게 좀 더 깔끔하고 좋음!
어차피 append를 해준 다음 해당하면 빼는거랑 똑같으니까
그래서 대충 
new_string.append(s[c])
해주고, 
if c==bomb_s[-1] and new_string[-n:]==bomb_s[:] 로 해주면 n이 1일때도 통과될 수 있고,
좀더 보기도 편함!
그리고 pop아니고 del stack[-n] 으로도 대체해줄 수 있음"""

if new_string==[]:
    print("FRULA")
else:
    print("".join(new_string))

"""
replace의 시간복잡도는 len만큼 나고, 또, 문자열자체를 새로 생성해주면서 계속 반복해주는 거라서
n*for문 만큼의 시간복잡도가 날 수 밖에 없음.
그래서 replace가 아닌 stack으로 문제를 풀어줘야함.
+로 스택.... 봤는데 뭐 어쩌라고 였는데
맨 뒷문자가 같을때를 기준으로, pop을 해주면 똑같다는걸 글 보고서야 알았음...
이런 접근을 아는게 중요한 듯함 어렵다 흑"""