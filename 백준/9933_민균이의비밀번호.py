
def ispaline(word1, word2):
    mid = len(word1)//2
    for i in range(mid):
        if word1[i] == word2[len(word2)-i-1] and word1[len(word1)-i-1] == word2[i]:
            pass
        else:
            return -1
    return mid

if __name__ == '__main__':
    N = int(input())
    texts = [input() for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(i,N):
            print(texts[i],texts[j])
            mid = ispaline(texts[i], texts[j])
            if mid != -1:
                print(len(texts[i]), end=' ')
                print(texts[i][mid])
                flag = 1
                break
        if flag == 1:
            break