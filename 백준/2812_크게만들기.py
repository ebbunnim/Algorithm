
if __name__ == '__main__':
    N,K = map(int, input().split())
    num = list(map(int,input()))
    stack = []
    cnt=0
    ans=''
    for i in range(N):
        while stack and stack[-1]<num[i] and cnt<K:
            stack.pop()
            K-=1
        stack.append(num[i])

    while cnt < K:
        stack.pop()
        K-=1

    for i in range(len(stack)):
        print(stack[i],end='')