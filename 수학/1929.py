n, m = map(int, input().split())

prime = [i for i in range(m+1)]
prime[1] = 0

for i in range(2, m+1):
    if prime[i]==0:
        continue

    for j in range(i*2, m+1, i):
        prime[j]=0

for i in range(n, m+1):
    if prime[i]!=0:
        print(prime[i])



