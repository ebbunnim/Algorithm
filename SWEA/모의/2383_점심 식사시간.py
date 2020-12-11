import sys
sys.stdin = open('input.txt','r')

from collections import deque

def make_waitings(group, step):
    waitings = []
    for p in group:
        waitings += [abs(p[0] - step[0]) + abs(p[1] - step[1]) + 1]
    waitings.sort(reverse=True)

    have_to_down = arr[step[0]][step[1]]
    working = deque()
    # 가장 빠른 애부터 넣어줄거야.
    # 처음에는 가장 3개를 꺼내. 그리고 만약에 대기에 있는애 시간이 마지막 시간 이전이라면 그떄동안 기다려


    if len(group)<=3:
        if len(group)==0:
            return 0
        else:
            return waitings[0]+have_to_down

    time = waitings[-1] # 첫번째 사람이 이제 계단을 내려갈거야

    while waitings or working:
        while True:
            if len(working)>=3:
                break
            if waitings:
                working.append(max(time,waitings.pop())+have_to_down) # 작업이 끝내는 시간을 넣어둠. 근데 기다리면 본래의 시간이 아니라 time 기준
                #print('working',working)

            else:
                break

        while working:
            if working[0]-time<=1:
                working.popleft()
            else:
                break # 시간이 더 흘러야 한다.

        time += 1

    return time


def dfs(start,x,group1):
    global minv
    if x==0:
        group2 = [p for p in people if p not in group1]

        # first
        val1=max(0,make_waitings(group1, steps[0]),make_waitings(group2, steps[1])) # 2 계단으로 나누되 더 늦은 시간이 최종 걸린 시간

        # second -> 계단 다르게 배치
        val2=max(0,make_waitings(group1, steps[1]),make_waitings(group2, steps[0]))

        # 그 중 어떤게 더 소요시간이 작냐
        minv = min(minv,min(val1,val2))

        return

    for i in range(start,len(people)):
        group1+=[people[i]]
        dfs(i+1,x-1,group1)
        group1.pop()

    return

def down():
    return


if __name__=="__main__":
    for t in range(int(input())):
        N = int(input())
        arr = [list(map(int,input().split())) for _ in range(N)]
        people=[]
        steps=[]
        for i in range(N):
            for j in range(N):
                if arr[i][j]==1:
                    people+=[(i,j)]
                elif arr[i][j]==0:
                    continue
                else:
                    steps+=[(i,j)]
        minv=1e9
        for x in range(len(people)//2+1):
            dfs(0,x,[]) # [], []으로 두 그룹으로 나뉘어지게 됨. 이 두 그룹을 step1, step2 둘다 커버하도록 만들어야 함.
            # 거리계산해서 대기줄로 세우기
            # 대기줄인 애들 시간 연산하기
            # down()

        print(f'#{t+1} {minv}')




