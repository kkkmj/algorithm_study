"""
N개의 정수로 이루어진 배열 A가 주어진다.
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
"""
#TODO 백트래킹, 브루트포스
import itertools #모든 순열을 구하는 라이브러리

n = int(input())
data = list(map(int, input().split()))

max_diff = 0 #최댓값 비교할 변수
#itertools 라이브러리를 이용해 가능한 순열 조합들 모두 생성 후 for문으로 탐색
for all_list in itertools.permutations(data,n):
    diff = 0 #이번 순열의 합
    for i in range(n-1): #만든 순열들 하나씩 합의 수 구하기
        diff += abs(all_list[i]-all_list[i+1])
    max_diff = max(max_diff, diff) #다 돈 값 중 최댓값 선별
print(max_diff) #최댓값 출력


"""
+ 처음에 문제를 잘못 이해해서 못풀었었는데
다시 보니까
맨 중간 값을 양 옆으로 보내고
제일 최댓값-제일 최솟값 한 뒤 계속 반복하는 식으로 해도 풀 수 있음 다만 구현을 잘 못했을 뿐..

n = int(input())
data = list(map(int, input().split()))

data.sort()
mini = data[0]
maxi = data[-1]
sum = maxi - mini

data = data[1:-1]
while(len(data)>0):
    if(len(data)!=1):
        a = data[0]
        b = data[-1]
        sum += maxi-a
        sum += b-mini
        maxi = b
        mini = a
        data = data[1:-1]
    else:
        a = data[0]
        sum += max(maxi-a, a-mini)
        break
print(sum)
"""
