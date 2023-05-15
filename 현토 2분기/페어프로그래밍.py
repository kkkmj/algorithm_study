n, m = map(int, input().split())
performances=list(map(int, input().split()))
pair = 0

start = 0
end = n-1

while start<end:
    if performances[start]+performances[end]>=m:
        pair+=1
    end-=1
    start+=1

print(pair)