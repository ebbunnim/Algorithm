import sys
sys.stdin = open("input.txt","r")


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    l = list(map(int, input().split()))


    # max를 찾고 그 이전요소들과의 차이를 더하고, 다음 track으로 넘어가야함.
    # 다음 track에서 max를 찾았는데, 그 인덱스 뒤에 요소들이 계속 작아진다면 0으로 처리하고 break해야


    # max_idx 함수를 정의한 이유는, 가장 큰 수 밑에까지의 track을 제외하고 계속 작아지는 수들이 아니라면 다시 다음 track에서 쓰이므로
    def max_idx(l):
        max = l[0]
        for i in range(len(l)):
            if l[i] >= max:
                max = l[i]
                max_idx_v = i
        return max_idx_v

    # 가장 큰 수를 알았다면, 그 이전까지의 요소들과의 차이를 모두 더해준다.
    # 주의할 것은 가장 큰수는 더해지면 안되는 수
    def difference(l, max_idx):
        diff = 0
        for i in range(max_idx):
            diff += l[max_idx] - l[i]
        return diff

    # 만약 가장 큰 수 뒤로 숫자들이 계속 작아진다면, 0으로 처리하고 연산을 멈추면 됨.
    def isdecrease(l):  # track이 계속 갱신되면서, 이전 리스트에서 max_idx_v+1 부터 시작되는 slicing된 애들이 들어갈 것
        if len(l) == 0:  # 맨 뒤에가 max뜨면 접근할 index가 없으므로 에러뜸. 이것을 방지.
            return True
        else:
            max = l[0]
            for i in range(len(l)):
                if l[i] <= max:
                    max = l[i]
                    continue
                else:
                    return False
            return True #모두 계속 작아지는 수였다면 True입니다.

    result = 0
    max_idx_v = max_idx(l)
    result += difference(l, max_idx_v)

# max 이후의 track이 존재하는 경우에 대하여
    temp = l[max_idx_v + 1:] #원래의 l은 왠만하면 건들이지 말자.
    while True: #재귀함수처럼 다음 track에 계속 접근
        if isdecrease(temp):
            break #여지껏 구했던 result 바로 반환하면 된다.
        else:  # 여기 계속 무한반복 되었었음... 이유는 temp를 다시 정의하지 않았기 때문. 재귀함수처럼 쓸 때 재정의에 민감해야!
            max_idx_v = max_idx(temp)
            result += difference(temp, max_idx_v)
            temp = temp[max_idx_v + 1:]  # l에서 찾는게 아니라 계속 슬라이싱되어서 새로운 list로 접근되어야

    print('#%d' % tc, result)
