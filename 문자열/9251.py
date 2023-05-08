import sys
string1 = ' '+ sys.stdin.readline().rstrip()
string2 = ' '+sys.stdin.readline().rstrip()

dp_str=[[0]*(len(string2)) for _ in range((len(string1)))]
#dp_str=[0]*len(string1)
for i in range(1, len(string1)):
    for j in range(1, len(string2)):

        if string1[i]==string2[j]:
            dp_str[i][j]=dp_str[i-1][j-1]+1
        else:
            dp_str[i][j]=max(dp_str[i-1][j], dp_str[i][j-1])
print(dp_str)
print(dp_str[len(string1)-1][len(string2)-1])

"""
lcs알고리즘이 있고, dp를 이용해서 푸는 문제
사실 알고리즘이 있는지는 모르겠다만 암튼 코드 보면 아는 것 처럼
문자열이 같다면 왼쪽 위에값 기준으로 +1 한값을 더해준다.
그 값을 계속 해서 맨 마지막 dpStr배열값 보면 알겠지만 어떤 문자열이 같게 걸려서 나왔는지 알 수 있다."""