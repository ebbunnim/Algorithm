
def getpi(sub_patterns):
    j = 0
    for i in range(1,len(sub_patterns)):
        while j > 0 and sub_patterns[i]!=sub_patterns[j]:
            j = PI[j-1]

        if sub_patterns[i] == sub_patterns[j]:
            j += 1
            PI[i] = j
    return

if __name__ == '__main__':
    patterns = list(input())
    L = len(patterns)
    res =0
    for a in range(L):
        sub_patterns = patterns[a:]
        PI = [0]*len(sub_patterns)
        getpi(sub_patterns)
        if res < max(PI):
            res = max(PI)
    print(res)
