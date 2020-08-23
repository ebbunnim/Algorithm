# 1. 처음에 cur.data 출력 및 stack에 쌓는다
# 2. 왼쪽 자식이 있으면 계속 stack에 push하고, 없으면 pop 시킨 뒤,
# 3. 부모 노드로 cur 이동하여 cur의 오른쪽 자식이 있으면 stack에 push하고
# 4. 없으면, pop시킨다.
# 2번 부터 반복
import sys
sys.stdin = open("input.txt", "r")

def inorder(i): #정점인 노드 번호로 시작함
    global path
    stack=[]
    stack.append(D[i])

    while stack:
        for i in range(1, N):
            if 2*i <= N:
                stack.append(D[2*i])
        path += stack.pop()
        for i in range(1, N):
            if 2*i+1 <= N:
                stack.append(D[2*i+1])
        path += stack.pop()


if __name__=="__main__":
    N = int(input())
    # 완전 이진트리 형식이므로 8번의 돌게된다.
    path=''

    D = [0]*(N+1) # 1,2,3, 각각 인덱스에 해당하는 값들이 담긴 리스트
    for i in range(1,N+1):
        tmp = input().split()
        D[i] = tmp[1]
    print(D)
    inorder(1)
    print(path)

