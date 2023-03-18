"""
14465번 소가 길을 건너간 이유 5

첫 줄에 N, K, B (1 ≤ B,K ≤ N)가 주어진다. 그 다음 B줄에는 고장난 신호등의 번호가 하나씩 주어진다.
정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지 출력한다.
"""
#TODO 슬라이딩 윈도우
n, k, b = map(int, input("n, k, b").split())

sign = [1 for i in range(n)] #신호등을 모두 1로 초기화
for i in range(b):
    sign[int(input())-1] = 0 #고장이 난 신호등은 0으로 변경

#슬라이딩 윈도우 알고리즘을 이용하여 연속 정상 신호등의 가장 큰 개수만큼 res에 할당
window = sum(sign[:k]) #초기값
res = window
for i in range(k, n):
    window += sign[i] - sign[i - k] #윈도우를 앞으로 1씩 이동
    res = max(res,window) #연속된 값이 더 큰게 존재하면 결과값 변경
answer = k - res #연속된 값 중 최대값 구해서, 수리해야할 신호등 개수 출력
print(answer)

"""계속 틀렸습니다가 나왔는데, 백준에서 input안에 어떠한 문자열이라도 있다면 틀렸습니다가 나오는 것 같다
즉, 맞았는데도 계속 뻘짓 한 것... 백준에서는 입력 안에 아무것도 넣지 말자..ㅠ"""