"""문자열 S가 주어졌을 때, S의 서로 다른 부분 문자열의 개수를 구하는 프로그램을 작성하시오.

부분 문자열은 S에서 연속된 일부분을 말하며, 길이가 1보다 크거나 같아야 한다.

예를 들어, ababc의 부분 문자열은 a, b, a, b, c, ab, ba, ab, bc, aba, bab, abc, abab, babc, ababc가 있고, 서로 다른것의 개수는 12개이다."""

S = input()

str_list = set()
for j in range(len(S)):
    for i in range(len(S)-(j)):
        str_list.add(S[i:i+j+1])

print(len(str_list))

"""주의점

1. 중복 제거 = set 자료구조
+set는 add로 추가
k라는 변수 굳이 쓸 필요 없이 위에 for문 그대로 쓰면됨..."""