import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    A,B=map(int,input().split())
    psum=[0]*(B+1)
    Nlist=[0]*(B+1)
    flag=0
    for i in range(1,B+1):
        for j in range(1,i+1):
            if i<=B:
                Nlist[j]=i
            else:
                flag=1
                break
        if flag:
            break
    print(Nlist)

