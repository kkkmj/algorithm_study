import sys
input = sys.stdin.readline
t = int(input())

def dfs(num, answer, i, n, form):
    if i==n-1:
        form+=str(num[i])
        answer.append(form)
        return

    dfs(num, answer, i + 1, n, form + str(num[i]) + " ")
    dfs(num, answer, i+1, n, form+str(num[i])+"+")
    dfs(num, answer, i + 1, n, form + str(num[i]) + "-")





for _ in range(t):
    answer=[]
    forms = []
    n = int(input())
    num = [i for i in range(1,n+1)]
    dfs(num, forms, 0, n, "")

    for i in range(len(forms)):
        k=1
        total=100
        temp=forms[i]
        t_m=[]
        t_n=[]

        while len(temp)!=k:
            if temp[k]=='+':
                t_m.append('+')
                t_n.append(temp[:k].replace(' ',''))
                temp = temp[k + 1:]
                k=1
            elif temp[k]=='-':
                t_m.append('-')
                t_n.append(temp[:k].replace(' ',''))
                temp=temp[k+1:]
                k=1
            else:
                k+=1
        temp=int(temp[:].replace(' ',''))
        if t_n:
            total=int(t_n[0])
            for l in range(1,len(t_n)):
                if t_m[l-1]=='+':
                    total+=int(t_n[l])
                else:
                    total-=int(t_n[l])
            if t_m[-1]=='+':
                total+=int(temp)
            else:
                total-=int(temp)
        if total==0:
            # print(t_n)
            # print(t_m)
            # print(forms[i])
            answer.append(forms[i])

    for a in answer:
        print(a)

    print()

"""
우선 애초에 n이 작아서 가능한 것 같긴한데
시간초과 안걸리고 바로 정답 때려주셔서 정말 감사합니다ㅎㅎ;
1. 파이썬을 활용해서 풀어주기
> eval() = 문자열 그대로 출력 가능 예를들어 "1+2-4" 이런걸 eval()에다 넣고 print해주면 -1 을 출력해줌

보통 eval()을 이용해서 풀었고, 찾아봤을 때 가장 마음에 드는 풀이는
굳이 숫자가 아닌 연산자 조합식을 사용해서 푼 경우. 어차피 숫자야 큰숫자 아니고 1~n까지 연산자만 바뀌는건데 굳이 숫자를 백트래킹 해줄 필요는 없음
그래서 연산자만 +,-,'', + 이런식으로 배열을 저장해준 다음, for문 돌려서 모든 수식 2중 loop로 돌려 버리기<<이것도 eval엿네;;

암튼 걍 모르겠고, 이 문제는 파이써닉하게 풀려면 eval를 쓰는 문제. eval라는게 있는 걸 알았고
솔직히 코테에서 이렇게 한 언어에 너무 유리한 문제는 안낼 것 같긴함
"""