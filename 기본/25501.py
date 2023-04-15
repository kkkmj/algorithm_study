t = int(input())

def isPalindrome(S, cnt, l):
    if(l>=cnt):
        return 1
    elif S[cnt]!=S[l]:
        return 0
    else:
        return isPalindrome(S, cnt+1, l-1)



for _ in range(t):
    S=input()
    n=isPalindrome(S, 0, len(S)-1)
    print(n)
