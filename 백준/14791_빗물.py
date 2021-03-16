import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    H,W=map(int,input().split())
    walls=list(map(int,input().split()))
    stack=[]
    acc=0

    for i in range(W):
        wall=walls[i]
        if not stack:
            stack+=[i]
            ubound=wall
            locate=i
            continue
        if wall==walls[stack[-1]]:
            continue
        if ubound>wall:
            stack+=[i]
        else:
            # trap의 조건 - stack 인덱스 관리하면서 가로 계산하고(maxv의 위치~들어올ele의 위치) 높이는 값을 기준으로 다음처럼 계산 : stack에서 pop될 애가 stack에 들어잇는 원소들의 maxv와 들어올 원소보다 작아야 하며, 카운트할 높이는 min(maxv,val)-walls[stack.pop()]
            while stack and walls[stack[-1]]<wall and walls[stack[-1]]<ubound:
                acc+=(min(wall,ubound)-walls[stack.pop()])
            stack+=[i]
            if wall>ubound:
                ubound=wall
                locate=i
    # 이렇게 하면 한쪽밖에 담을 수 없음. max로 큰 놈 나와버리면, 걔를 기준으로 스택에 작은 값들은 쌓일 수밖에 없음.
    # 예시 1은 되지만, 예시2는 되지 않는 이유가 됨.
    print(acc)

