def getpi():
    j = 0
    for i in range(1,L):
        while (j>0 and pattern[i] != pattern[j]):
            j = PI[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            PI[i] = j
    return

def kmp():
    j = 0
    for i in range(len(text)):
        while (j>0 and text[i] != pattern[j]):
            j = PI[j-1]

        if text[i] == pattern[j]:
            if j == L-1: # 끝까지 왔다면
                print(1)
                return
            else:
                j += 1
    print(0)

if __name__ == '__main__':
    text = list(input())
    pattern = list(input())
    L = len(pattern)
    PI = [0]*L

    getpi()
    kmp()
