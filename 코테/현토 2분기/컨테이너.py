"""
얘는
1. 정렬해서 틀렸고
2. replace써서 틀렸음 ex) 문자 안에 안문자가 여러개 있을 수도 있음
"""
n = int(input())
words = [input().strip() for _ in range(n)]
words.sort(key=lambda x:len(x)) #...이거 sort해주면 안됐네ㅋㅋㅋㅋㅋㅋ 왜냐면 사전순 그래도 해주는거니까..아..ㅋㅋ틀렷다
# 사실 누적합 왜썼냐는 질문 보다는 2번 왜이렇게 풀었는지가 너무너무 궁금할 듯 나같아도 궁금하다..sibal
min_len = len(words[0])

for i in range(n):
    flag = 0
    word = words[i]
    if len(words[i])<min_len*2:
        pass
    else:
        for j in range(i):
            if words[j] in word[1:-1]:
                word = word.replace(words[j],"") #우선 이거 replace 해주면 안됨
                #그럼 어떻게 구현을 할 것이냐... ㅠ
                for k in range(i):
                    if word==words[k]:
                        flag=1
                        break
            if flag:
                break

    if not flag:
        print("No")
    else:
        print("Yes")