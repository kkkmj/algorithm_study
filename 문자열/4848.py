import sys

input = sys.stdin.readline

set_num0 = "{}"
set_num1 = "{{}}"

set_num_info=[0,0,1]

for i in range(3,16):
    sumSet = sum(set_num_info)
    set_num_info.append(i-1+sumSet)
set_num_info[0]=-1

set_num_dict={}
set_num_dict[0]=set_num0
set_num_dict[1]=set_num1

for i in range(2, 16):
    set_num_dict[i]="{"+set_num_dict[i-1][1:-1]+","+set_num_dict[i-1]+"}"

test_case = int(input())
for _ in range(test_case):

    input_num1 = list(input()[1:-2].rstrip().split(','))
    input_num2 = list(input()[1:-2].rstrip().split(','))
    num1, num2 = len(input_num1)-1, len(input_num2)-1
    if input_num1[0]=='':
        num1=-1
    if input_num2[0]=='':
        num2=-1
    num1 = set_num_info.index(num1)
    num2 = set_num_info.index(num2)
    sum_num=num1+num2

    print(set_num_dict[sum_num])

"""
1. 저 setNum을 굳이 dict에 안해도 되는게
어차피 인덱스 번호에 따라 해당 값이 출력만 하면  되기 때문에 상관이 없다.
인덱스 번호 = 출력해야할 값 인 경우 자꾸 이걸 까먹고 굳이 자료구조를 더 쓰는데 그러지 말자.
2. 오히려 ,의 경우가 dict를 해야하는 부분이다. index 라는 함수는 처음부터 끝까지 탐색해야 되기 때문에
index라는 함수를 써야되는 순간 index로 하지 말고 dict를 쓰자. 
그래서 이것도 굳이 반복문 두번 돌릴 필요 없이, len을 구해서 lendict를 만들어줬다.
추가로 문자열길이에 해당하는 값이 인덱스 번호가 출력이 되도록 해야하기 때문에
dict[i]=len 를 해줘야될게 아니라,
dict[len]=i 를 해야 좀더 효율적인 탐색이 가능하다!
"""