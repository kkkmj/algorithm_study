"""세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.

그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.

괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오."""
s=input().split('-')
num=[]
for i in s:
    sum=0
    l=i.split('+')
    for j in l:
        sum+=int(j)
    num.append(sum)

n=num[0]
for i in range(1,len(num)):
    n-=num[i]
print(n)

"""나는 박대가리야...ㅠㅠㅠ
우선 문제 접근부터 잘못했는데
이런식으로 수식을 준다면 파이썬에서는 split이란 미친 기능을 이용해서 숫자를 나눠주는게 좋음 굳이 if i=='+'이딴짓 안해도 됨
그리고 접근자체도 그냥 - 전에 있는거 무조건 +로 하면 되는데 일단 생.각 이란걸 하고 문제를 푸는게 좋을 것 같음
단순히 그리디 이것만 보고 어.... 순열 어케해야하지 이러지 말고 어떻게 하는게 제일 최적의 해일까를 생각하고 한 다음에 하기.
"""