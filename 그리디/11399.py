import sys
input = sys.stdin.readline
n = int(input())
time = list(map(int, input().split()))
time.sort()
wait=0
for i in range(len(time)):
    wait+=time[i]
    time[i]=wait


print(sum(time))

"""개 쩌는거.. 는 아니고 수식 제대로 활용해서 하는법 알았음! 좀 더 예쁜 방식!

애초에 문제 자체가 a1 + (a1+a2) + (a1+a2+a3) + ...
이런식임
즉 a1은 n번만큼 더해주고, a2는 n-2번만큼 더해주고 a3은 n-3번만큼 더해주고
그래서 최소값이 되려면 n번만큼 더해주는 값을 가장 작게, n-(n-1)번만큼 더해주는 값을 가장 크게 하면 된다는 뜻!
그래서 걍 그리디 해주고 for문 돌리면서 time.pop 하면서 i+1 씩 곱해주면 됨.
pop은 맨 끝값 빼주는 거니까 맨끝값*1, n-(n-2) * 2 이런식으로
점화식 등 기존의 수학 식을 좀 더 생각해보자!
"""