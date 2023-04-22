t = int(input())

for _ in range(t):
    ans=''
    r, S = map(str, input().split())
    r = int(r)
    for ch in S:
        for _ in range(r):
            ans+=ch

    print(ans)
