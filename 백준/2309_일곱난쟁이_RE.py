import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def comb(src,cnt,sumv,stack):
    if cnt==7:
        if sumv==100:
            return stack
        return
    for dst in range(src+1,9):
        stack+=[dst]
        res=comb(dst,cnt+1,sumv+Nlist[dst],stack)
        if res:
            return stack
        stack.pop()

if __name__ == '__main__':
    Nlist=[int(input()) for _ in range(9)]
    for x in sorted([Nlist[x] for x in comb(-1,0,0,[])]):
        print(x)
