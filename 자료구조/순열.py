list1 = [1, 2, 3, 4]
n = 2
permut = []
stack = [([x],[i]) for i, x in enumerate(list1)]

while stack:
    per, idx_list = stack.pop()

    if len(per) == n:
        permut.append(per)
        continue
    for i in range(len(list1)):
        if i not in idx_list:
            stack.append((per+[list1[i]], idx_list+[i]))


for p in sorted(permut):
    print(p)