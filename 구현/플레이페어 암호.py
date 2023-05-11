import sys

input = sys.stdin.readline

message = input().strip()
key = list(input().strip())
message_list = []

key += [chr(i) for i in range(65, 74)] + [chr(i) for i in range(75, 91)]
key = list(set(key))
answer = ''

i = 0
while i < len(message):
    if i == len(message) - 1:
        message_list.append(message[i] + 'X')
        i += 1
    elif message[i] != message[i + 1]:
        message_list.append(message[i] + message[i + 1])
        i += 2
    else:
        if message[i] != 'X':
            message_list.append(message[i] + 'X')
            i += 1
        else:
            message_list.append(message[i] + 'Q')
            i += 1


for i in range(len(message_list)):
    idx1 = key.index(message_list[i][0])
    idx2 = key.index(message_list[i][1])

    if idx1 // 5 == idx2 // 5:
        answer += key[(idx1//5)*5 + (((idx1%5)+1)%5)]
        answer += key[(idx2//5)*5 + (((idx2%5)+1)%5)]

    elif idx1 % 5 == idx2 % 5:
        answer += key[(idx1 + 5) % 25]
        answer += key[(idx2 + 5) % 25]

    else:
        answer += key[((idx1//5)*5) + (idx2 % 5)]
        answer += key[((idx2//5)*5) + (idx1 % 5)]

print(answer)


"""
1. 효율성 생각하면서 했더니 이게 맞나.. 싶었지만, 키 자체는 25밖에 안됐기 때문에 index써서 했음. 결론적으론 효율성 생각하면서 잘 한듯!
2. 문자열 바꾸는 것도 잘했음! 좀만 더 예쁠 수 있을 것 같긴한데... 이정도면 낫밷인듯?

런타임 에러가 났는데 처음 구현을 (아니 사실 그냥 틀렷음)
for k in range(len(message_list)):
    c1_m=message_list[k][1]
    c2_m=message_list[k][1]
    c1=key.index(message_list[k][0])
    c2=key.index(message_list[k][1])
    if c2//5==c1//5:
        if c1%5<4 and c2%5<4:
            c1_m=key[c1+1]
            c2_m=key[c2+1]
        elif c2%5==4:
            c1_m=key[c1+1]
            c2_m=key[c2-4]
        elif c1%5==4:
            c1_m=key[c1-4]
            c2_m=key[c2+1]
    
    elif c1%5==c2%5:
        if c1<20 and c2<20:
            c1_m=key[c1+5]
            c2_m=key[c2+5]
        elif c1>19:
            c1_m=key[c1-20]
            c2_m=key[c2+5]
        elif c2>19:
            c1_m=key[c1+5]
            c2_m=key[c2-20]
    else:
        c1_m=key[(c1//5)*5 +(c2%5)]
        c2_m=key[(c2//5)*5+(c1%5)]
    message_list[k]=c1_m+c2_m
    
이딴식으로 했음 ㅎㅎ;;
일단 식으로 만들어서 해줄 생각을 못하고, if문으로 나눠서 했는데 이것때문에 못잡은 케이스가 있어서 런타임 에러가 났음. 아직도 어디서 났는지는 모름 ㅎㅎ;;
암튼 이렇게 조건문으로 더럽게 하지말고 %기를 활용하면 배열 안에서 깔끔하게 처리해줄 수 있음!
이런거 전에도 봤던 것 같은데 습관이 안되는 것 같음. 계속 생각해주자!
예를 들어 
행을 넘어가면 %행 해줘서 행 넘어가는거 방지해주고
열은 %열 해줘서 열 넘어가는거 방지해주기!! 배열과 인덱스 접근에서 필수적임!
그리고 더럽게 저렇게 ㅎ ㅏ지말고 answer 만들어서 해주는 것도 정말 좋은 방법인듯
"""
