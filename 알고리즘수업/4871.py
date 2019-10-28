import sys
sys.stdin = open("4871input.txt","r")

def search_map(start):  #행번호
    global result
    visited[start]=1  #방문한곳은 1
    for next in range(1,mynode+1): #시작노드에 등록된 도착노드 검색
        if mymap[start][next] == 1 and visited[next] == 0: #안가본곳
            if next == end_node:
                result = 1 #갈 수 있는곳
                return #검색 중단
            search_map(next) #다음 노드로 가서 검색


TC = int(input())
for tc in range(1, TC+1):
    mynode, myline = map(int,input().split())
    mymap = [ [0]*(mynode+1) for _i in range(mynode+1) ]  #2차원배열
    #
    # print("myline",myline)
    for i in range(myline): #간선의갯수만큼 읽기
        start_node, end_node = map(int, input().split())
        mymap[start_node][end_node] = 1

    start_node, end_node = map(int, input().split()) #검색시작, 검색끝
    visited = [0]*(mynode+1)  #방문했던곳 표시용.
    result = 0 #갈수있으면 1 없으면 0

    search_map(start_node)  # 재귀함수
    print("#%d %d" % (tc, result))
