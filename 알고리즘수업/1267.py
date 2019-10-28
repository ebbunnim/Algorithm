import sys
sys.stdin = open("1267input.txt","r")

TC = 3
for tc in range(1, TC+1):
    mynode, myline = map(int, input().split()) # 노드수, 간선수,
    mymap = [ [0]*(mynode+1)  for i in range(mynode+1) ]  #2차원 맵 생성
    #간선정보입력
    data = list( map(int,input().split()) )   # 2 1 1 3
    n = int(len(data)/2)  # 나누기 결과는 실수 -> 정수로 변환
    for i in range(n):
        start = data[i*2] #짝수      0,2,4,6,8
        end = data[i*2 + 1] # 홀수   1,3,5,7,9
        mymap[end][start] = 1

    result=[] #작업경로 저장
    while True:
        if len(result) == mynode: #전체 노드가 경로에 모두 저장되면 검색 중단
            break
        start_col = [] #
        for col in range(1, len(mymap)): #모든 칼럼을 검색
            if  1 not in mymap[col] and col not in result: #작업경로에 등록안된
                start_col.append(col) #출발가능한 노드 등록

        for col in start_col:
            result.append(col) # 출발가능한 노드를 작업경로에 등록
            for row in range(len(mymap)):
                mymap[row][col]=0  #출발하는 노드로 연결되는 정보 삭제

    print("#%d"%tc, end=" ")
    for i in result:
        print("%d"%i, end=" ")
    print()

