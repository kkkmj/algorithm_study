import sys
import heapq
n = int(sys.stdin.readline())
nums= []
for _ in range(n):
    x = int(sys.stdin.readline())
    if not x:
        if len(nums)==0:
            print(0)
        else:
            print(heapq.heappop(nums))
    else:
        heapq.heappush(nums,x)


"""
1. 리스트가 가장 느리고, 그다음이 큐가 느림
그리고 우선순위 큐보다 힙큐가 더 빠름
 그래서 최소값 구할땐 힙큐
 힙큐는 보통 최소힙 이고, 최대힙으로 하려면 -를 붙여서 최대힙을 구현할 수 있음
 또, 여기서 시간초과가 난 이유는 sys.stdin.readline()이 아닌
 input()을 통해 입력값을 받아서인데
 왜그런지 모르겠다
 이거에 관해서는 알아보자."""