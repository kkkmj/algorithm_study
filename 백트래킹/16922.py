nums = [1, 5, 10, 50]

n = int(input())
kind = set()
answer = []


def back(start):
    if len(answer) == n:
        s = sum(answer)
        kind.add(s)
        return

    for i in range(start,len(nums)):
        answer.append(nums[i])
        back(i)
        answer.pop()


back(0)
print(len(kind))

"""
combination_with_replacement
이게 중복조합으로 itertools의 저걸 이용해서도 풀 수 있음.
중복 조합이 있는줄 몰랏네,,,멌쓲"""