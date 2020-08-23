
def getpi(pattern):
    j = 0
    for i in range(1,L): # j=0, i=1을 비교하므로 길이 2인 수열부터 시작한다는 의미
        while (j>0 and pattern[i]!=pattern[j]):
            j = P[j-1]
        if (pattern[i] == pattern[j]):
            j += 1
            P[i] = j
    return


def kmp():
    j = 0
    for i in range(len(text)):
        # 일치하지 않는(Fail) 순간, 일치할때까지 back시킨다.
        while (j>0 and text[i]!=pattern[j]):
            j = P[j-1]

        if text[i] == pattern[j]:
            if (j == L-1):
                ans.append(i-L+1+1)
                j = P[j]
            else:
                j += 1
    return


if __name__ == '__main__':
    text = list(input())
    pattern = list(input())
    TL = len(text)
    L = len(pattern)
    P = [0]*L
    ans = []
    getpi(pattern)
    kmp()
    print(len(ans))
    for e in ans:
        print(e, end=' ')