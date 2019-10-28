import sys
sys.stdin = open('input.txt','r')

def preorder(t):
    global cnt
    stack = []
    stack.append(t)

    while 0<len(stack):
        data = stack.pop()
        for i in range(E):
            if D[i][0] == data[1]:
                stack.append(D[i])
                cnt += 1

if __name__ == "__main__":
    for tc in range(1, int(input())+1):
        E, val = map(int, input().split())
        # print((E, val))
        temp = list(map(int, input().split()))
        start=[0]*E; end=[0]*E
        for i in range(2*E):
            if not i%2:
                start[i//2] = temp[i]
            else:
                end[i//2] = temp[i]
        D = {}
        for i in range(E):
            D[i] = (start[i],end[i])
        print(D)
        cnt = 1
        for i in range(E):
            if D[i][1] == val: #End에서부터 시작해야
                preorder(D[i])
        print('#%d %d' % (tc,cnt))