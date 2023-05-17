n = int(input())
list1 = list(map(int, input().split()))
list1.sort()
m = int(input())

def binary_search(end, start, target):
    if start > end:
        return 0
    mid = (end+start)//2
    if target == list1[mid]:
        return 1
    elif target>list1[mid]:
        return binary_search(end, mid+1, target)
    else:
        return binary_search(mid-1, start, target)



for i in map(int, input().split()):
    print(binary_search(n-1, 0, i) )

"""
더이상 그 밑에 있는 걸로 가지 않게 하려면 return을 해주자.
return은 약간 break와 같은 걸로 그 값 자체를 return해주겠다는 뜻이 아닐 수도 있음
return에 대해서 좀 더 생각해봐야할 필요가 있는 듯
아직 재귀를 정확히 이해 못하고 있음
"""