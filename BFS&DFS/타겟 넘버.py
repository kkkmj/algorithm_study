numbers = list(map(int, input().split()))
target = int(input())
n=len(numbers)
answer=[]
def dfs(i, sum):
    if i==n-1:
        if sum+numbers[i]==target:
            answer.append(sum)
        if sum-numbers[i]==target:
            answer.append(sum)
        return
    dfs(i+1, sum+numbers[i])
    dfs(i+1, sum+numbers[i]*(-1))

dfs(0, 0)
print(len(answer))
