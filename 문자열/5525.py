import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
S = input().strip()
count = 0
answer=0
i=0

while i < m-2:
    if S[i:i+3]=='IOI':
        count+=1
        i+=2
        if count == n:
            answer+=1
            count-=1
    else:
        i+=1
        count=0

print(answer)

