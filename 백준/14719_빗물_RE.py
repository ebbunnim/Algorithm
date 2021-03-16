import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    H,W=map(int,input().split())
    walls=list(map(int,input().split()))
    stack=[]
    acc=0
    for i in range(W):
        while stack and walls[stack[-1]]<walls[i]:
            idx=stack.pop()
            if stack==[]:
                break
            acc+=(min(walls[stack[-1]],walls[i])-walls[idx])*(i-stack[-1]-1)
        stack.append(i)
    print(acc)


