N = int(input())
b = bin(N)[2:][::-1]

answer = 0
for i in range(len(b)):
    answer+=(int(b[i])*(3**i))

print(answer)
