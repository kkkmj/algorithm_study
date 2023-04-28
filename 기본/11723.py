import sys

input = sys.stdin.readline
S = set()


def madd(x):
    S.add(x)


def mremove(x):
    if x in S:
        S.remove(x)


def mcheck(x):
    if x in S:
        print(1)
    else:
        print(0)


def mtoggle(x):
    if x in S:
        S.remove(x)
    else:
        S.add(x)


def mall():
    S.clear()
    S.update({i for i in range(1, 21)})


def mempty():
    S.clear()


m = int(input())
for _ in range(m):
    com = input().rstrip().split()
    if com[0] == "add":
        madd(int(com[1]))
    elif com[0] == "remove":
        mremove(int(com[1]))
    elif com[0] == "check":
        mcheck(int(com[1]))
    elif com[0] == "toggle":
        mtoggle(int(com[1]))
    elif com[0] == "all":
        mall()
    elif com[0] == "empty":
        mempty()
