"""요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오."""
#TODO 큐
n, k = map(int, input().split())

que = [i for i in range(1, n+1)]
ans = []
now = 0

while que:
    now+=k-1
    if now > len(que) - 1:
        now %= len(que)
    ans.append(que.pop(now))
list_to_str = list(map(str,ans))
print('<'+', '.join(list_to_str)+'>')


"""
큐는 포인터 느낌을 잘 살려서 풀어야하는 것 같음
좀더 간결하게 줄이자면 
    if now > len(que) - 1:
        now %= len(que)
이부분을 그냥 if안쓰고 애초에 처음부터
now = (now + k -1) % len(que)
해주면 된다는점 왜냐면 어차피 넘든 안넘든 나누기 해도 똑같기 때문

또, 출력 형식에 대해서도 이렇게 할 수 있구나를 처음 알았음
문자열 .join 에 대해서 알기. 리스트 사이마다 .join 앞에잇는 애들을 넣어줄 수 있음
"""