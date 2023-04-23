S=input()
S=list(S.upper())
S.sort()
dic={}
max=0
ans='?'
for i in range(len(S)):
    if S[i] in dic.keys():
        dic[S[i]]+=1
    else:
        dic[S[i]]=1
for k in dic:
    if max<dic[k]:
        max=dic[k]
        ans=k
    elif max==dic[k]:
        ans='?'

print(ans)