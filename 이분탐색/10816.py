n = int(input())
cards = list(map(int, input().split()))

m = int(input())
problems = list(map(int, input().split()))

card_dict = {}
for i in cards:
    if i in card_dict:
        card_dict[i]+=1
    else:
        card_dict[i]=1
answers = []
for i in problems:
    if i in card_dict:
        answers.append(card_dict[i])
    else:
        answers.append(0)

print(' '.join(map(str, answers)))

"""
for element in lst:
    try:
        dictionary[element] += 1
    except KeyError:
        dictionary[element] = 1

와 쩐다 in 자체가 그래도 시간을 좀 잡아먹으니 아예 예외로 해놨네ㅋㅋㅋㅋㅋ        
"""