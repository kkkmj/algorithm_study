import itertools

while True:
    temp = list(map(int, input().split()))
    k = temp[0]
    if k==0:
        break
    S = temp[1:]
    for i in itertools.combinations(S, 6):
        print(*i)
    print()

"""
k, *s
이런식으로 해서 정수 + 배열 같이 받을 수 있음.
어쨌든 배열의 주소값이 *s 니까"""