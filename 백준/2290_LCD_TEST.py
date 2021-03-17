import sys
sys.stdin = open('input.txt','r')

def check(n):
    if n=='1':
        return one(w,h)
    if n=='2':
        return two(w,h)
    if n=='3':
        return three(w,h)
    if n=='4':
        return four(w,h)
    if n=='5':
        return five(w,h)
    if n=='6':
        return six(w,h)
    if n=='7':
        return seven(w,h)
    if n=='8':
        return eight(w,h)
    if n=='9':
        return nine(w,h)
    if n=='0':
        return zero(w,h)

def one(w,h):
    s=[[' ']*w for _ in range(h)]
    for i in range(1,h//2):
        s[i][w-1]='|'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    return (list(map(lambda x : ''.join(x), s)))

def two(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][0]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def three(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def four(w,h):
    s=[[' ']*w for _ in range(h)]
    for i in range(1,h//2):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    return (list(map(lambda x : ''.join(x), s)))

def five(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][0]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def six(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][0]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def seven(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][w-1]='|'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    return (list(map(lambda x : ''.join(x), s)))

def eight(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def nine(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h//2][j]='-'
    for i in range(h//2+1,h-1):
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

def zero(w,h):
    s=[[' ']*w for _ in range(h)]
    for j in range(1,w-1):
        s[0][j]='-'
    for i in range(1,h//2):
        s[i][0]='|'
        s[i][w-1]='|'
    for i in range(h//2+1,h-1):
        s[i][0]='|'
        s[i][w-1]='|'
    for j in range(1,w-1):
        s[h-1][j]='-'
    return (list(map(lambda x : ''.join(x), s)))

if __name__ == '__main__':
    s,n=input().split()
    w,h=int(s)+2,2*int(s)+3
    res=['']*len(n)
    for i in range(len(n)):
        res[i]=check(n[i])
    for e in map(lambda x:' '.join(x),zip(*res)): #line별로 출력이 되니까, 같은 줄에 있는 모든 컬럼의 값들을 다 뽑아서 더한다.
        print(e)