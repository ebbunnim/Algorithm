import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def trap(walls,length):
    stack=[]
    maxv=0
    acc=0
    for i in range(length):
        wall=walls[i]
        if not stack:
            stack.append(wall)
            maxv=wall
            continue
        # trap : 양쪽이 막혀있어야 함. 현재 stack에 담겨있는 원소중 maxv보다 더 높은 maxv나올 때는 물을 trap할 수 있음. min(maxv,next_ele)-stack.pop() 으로 빗물 담는다.
        # 그런데, 이처럼 trap하면 전체 빌딩 중에 가장 큰 애를 기점으로 더이상 진행이 안됨. 즉, 더 높은 빌딩 발견 못하므로 stack에 나머지 빌딩 담다가 끝남. 이래서 좌우로 가는 것임.
        if wall>=maxv:
            while stack and stack[-1]<wall:
                acc+=min(maxv,wall)-stack.pop()
            maxv=max(wall,maxv)
            stack.append(wall)
        else:
            stack.append(wall)
    return acc

if __name__ == '__main__':
    H,W=map(int,input().split())
    walls=list(map(int,input().split()))
    stack=[]
    maxv=acc=0
    for i in range(W):
        if walls[i]>maxv:
            max_idx=i
            maxv=walls[i]
    # left + right
    print(trap(walls[:max_idx+1],max_idx+1)+trap(walls[max_idx:W][::-1],W-max_idx))

