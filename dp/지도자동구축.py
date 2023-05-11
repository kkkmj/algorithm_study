import sys
n = int(sys.stdin.readline())

i=2

for _ in range(n):
    i+=(i-1)

print(i*i)