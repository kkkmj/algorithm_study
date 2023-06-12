n = int(input())
balloons = list(enumerate(map(int, input().split())))

i = 0
answer = []
for _ in range(n):
    balloon, num = balloons[i]
    answer.append(balloon+1)
    del balloons[i]
    if not balloons:
        break
    if num > 0:
        num-=1
    i = (i+num)%len(balloons)

print(* answer)
