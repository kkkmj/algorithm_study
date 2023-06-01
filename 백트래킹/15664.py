n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

answer = set()
temp = []
def dfs(start, temp):
    if len(temp) == m:
        answer.add(tuple(temp))
        return

    for i in range(start, n):
        temp.append(nums[i])
        dfs(i+1, temp)
        temp.pop()

dfs(0, temp)

answer=list(answer)
answer.sort()

for i in answer:
    print(*i)