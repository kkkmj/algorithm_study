l, c = map(int, input().split())
chars = list(map(str, input().split()))

vs = ['a', 'e', 'i', 'o', 'u']
temp = []
chars.sort()

#순열x, 조합
def dfs(start):
    if len(temp)==l:
        if 1<len(set(temp)-set(vs))<l:
            print(''.join(map(str,temp)))
        return

    for i in range(start, c):
        if not chars[i] in temp:
            temp.append(chars[i])
            dfs(i)
            temp.pop()

dfs(0)

