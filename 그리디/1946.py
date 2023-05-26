import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    applicants = [list(map(int, input().split())) for _ in range(n)]
    answer=1
    applicants.sort()
    min2 = applicants[0][1]

    for i in range(1,n):
        if min2>applicants[i][1]:
            min2 = applicants[i][1]
            answer+=1

    print(answer)


"""와 쩐다 이걸 a,b가 아니라 인덱스, 순위 로 정렬없이 풀 수 있구나 천잰가..??

암튼 머리가 안돌아가서 정답을 보고 하지는 않았고, 블로그 검색을 하면서 사람들이 해결생각을 한것 위주로 봤다.
그냥 정렬을 하면, 우선 무조건 서류 순위는 뒤에 사람이 밀리게 된다. 즉, 서류 정렬 기준 면접 점수만 보면 된다는 것!
사실 이 생각을 하는게 젤 오래걸리는 것 같다. 서류 순위로 정렬을 때리면 면접 순위만 보면 된다는게.
그 다음은 뭐, 그 위에를 기준으로 면접순위 젤 작은사람을 박아두면 그 밑에 있는 사람은 다 걸러진다.

"""