from collections import deque

n, w ,L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque()
t = 0
while trucks:
    t+=1
    now = 0
    front = trucks[0]
    if now+front>L:
        

