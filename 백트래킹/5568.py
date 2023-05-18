import itertools
n = int(input())
k = int(input())
cards = [int(input()) for _ in range(n)]
card_num = set()
for ps in itertools.permutations(cards, k):
    temp=""
    for num in ps:
        temp+=str(num)
    card_num.add(temp)
print(len(card_num))
