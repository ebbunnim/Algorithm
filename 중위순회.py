# ※ 완전이진트리 : 노드 삽입할 때 왼쪽부터 차례대로 추가하는 이진트리
# ※ 중위 순회(Inorder Traversal)
#  - LDR의 순서로 순회하는 방법
#  - 현재 노드의 왼쪽 방문 후 방문한 노드의 값을 학인한 후 오른쪽 노드를 방문한다.
#  - 만약 지속적으로 왼쪽 서브트리 값이 있다면 왼쪽 노드를 계속 방문해 단말 노드까지 접근한다. 그런 후 단말 노드의 값을 확인한 후
#    순차적으로 올라가면서 값을 확인하고 올라가는 길에 오른쪽 서브트리가 있는 노드를 만난다면 오른족 서브트리 방문 후 그 노드가
#    왼쪽 노드가 있나 확인하고 있다면 다시 왼쪽 노드의 단말노드까지 접근 후 값 확인을 하면서 올라온다.
#    즉 왼쪽 단말노드 접근 후 순차적으로 올라가면서 값 확인 -> 올라가는길에 오른쪽 노드가 있다면 오른쪽 노드 방문 후 왼쪽
#    단말노드 접근 후 순차적으로 올라가면서 값 확인을 반복한다.
# 완전 이진트리를 표현한 1차원 배열에서 인덱스 관계이다.

# 중위 순회(inorder traversal)
# 1) 더 이상 진행할 수 없을 때까지 왼쪽 방향으로 이동하여 내려간다.
# 2) 그 노드를 '방문'하고 오른쪽 자식 노드로 이동한 뒤 계속한다.
# 3) 이때 오른쪽으로 이동할 수 없을 때에는 한 노드 뒤로 되돌아간다.

# 반면 완전 이진 트리는 배열로 표현해도 메모리 낭비가 없기 때문에 노드를 이용하여 구현하지 않고 배열로 표현할 때가 많습니다.

import sys
sys.stdin = open("input.txt", "r")

def inorder(x): #x는 노드의 번호를 의미
    global path
    if x <= N:
        inorder(2*x)
        path += D[x]
        inorder(2*x+1) # 오른쪽으로 뻗을 수 있다면 뻗어라

if __name__=="__main__":
    N = int(input())
    # 완전 이진트리 형식이므로 8번의 돌게된다.
    path=''

    D = [0]*(N+1) # 1,2,3, 각각 인덱스에 해당하는 값들이 담긴 리스트
    for i in range(1,N+1):
        tmp = input().split()
        D[i] = tmp[1]
    print(D)
    # 완전 이중 트리라는 것이 왼쪽 노드가 먼저 존재하고 오른쪽 노드는 존재할수도, 안존재할 수도 있다는 의미
    inorder(1)
    # 반환하면 상위노드로 돌아감. 그리고 이미 반환한 값이었다면 이미 path에 추가되어 있음을 의미
    # DFS처럼 푸는데 DFS의 visited를 취급하지 않아도 인덱스에서 재귀반환하면 상위노드로 올라가므로 중복처리되지 않음
    # 즉 더이상 아래로 내려갈 수 없다면, path에 방문처리하고 상위노드로 값을 반환해 시작함
    print(path)
