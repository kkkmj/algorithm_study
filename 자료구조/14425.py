"""총 N개의 문자열로 이루어진 집합 S가 주어진다.

입력으로 주어지는 M개의 문자열 중에서 집합 S에 포함되어 있는 것이 총 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 문자열의 개수 N과 M (1 ≤ N ≤ 10,000, 1 ≤ M ≤ 10,000)이 주어진다.

다음 N개의 줄에는 집합 S에 포함되어 있는 문자열들이 주어진다.

다음 M개의 줄에는 검사해야 하는 문자열들이 주어진다.

입력으로 주어지는 문자열은 알파벳 소문자로만 이루어져 있으며, 길이는 500을 넘지 않는다. 집합 S에 같은 문자열이 여러 번 주어지는 경우는 없다."""

#TODO 해시테이블(set)
n, m = map(int, input().split())

data = []
sum = 0
for i in range(n):
    data.append(input())
for j in range(m):
    if input() in data:
        sum+=1
print(sum)

"""
그냥 list로 풀었는데
여기서 알아야 될 점은 set과 dict는 해시테이블 구조라서 보통 빠름
그래서 in 연산자를 쓸때 list에 비해 set가 훨씬 빠른 것

list는 맨 앞부터 끝까지 검사를 하고, set은 맨 앞이든 뒤든 시간이 일정함
그래서 찾는 거는 해시테이블인 set를 이용해서 시간을 빠르게 할 수 있음

data = set()
sum = 0
for i in range(n):
    data.add(input())
for j in range(m):
    if input() in data:
        sum+=1
print(sum)

이렇게 set로 푸는게 시간이 무려 약 5배나 차이남
그래서 해시테이블을 언제 사용하는게 좋은지를 알아야 한ㄴ다~
"""