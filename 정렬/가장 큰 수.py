numbers = list(map(int, input().split()))


numbers=[str(i)*3 for i in numbers]
numbers.sort(reverse=True)
#numbers.sort(key=lambda x : (x[0], x[1], x[2]), reverse=True)
numbers=[i[:len(i)//3] for i in numbers]
print(numbers)

"""
1. 문자열은 된다. 근데 왜?
*3을 해주는 이유는 어차피 3자리수 뒤로는 같은 숫자가 반복된다.
아스키 코드로 비교해줄 때 맨 앞에서 부터 비교를 시작하고, 이미 앞 3자리수에서 비교가 끝났기 때문에 굳이 해줄 필요가 없다. 
그래서 문자열로 바꿔주고, *3을 해서 3개로 만든다음, reverse=True를 해주면 끝!
"""