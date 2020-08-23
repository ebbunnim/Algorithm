import sys
sys.stdin = open("input1.txt", "r")

def iswall(x,y,w,h):
    if w <= x or x <= 0: #= 써주는 것 주의!
        return True
    if h <= y or y <= 0:
        return True
    return False

def turn(p,q,w,h): #어떨때 turn 함수를 만남? turn함수를 만나면?
    global dp #전역변수화! 계속 상호작용 해야하므로
    global dq
    x_direction = [1, -1]
    y_direction = [1, -1]

    if p == w:
        dp = x_direction[1] #얘로 쭉 더해야
    elif p == 0:
        dp = x_direction[0]
    if q == h:
        dq = y_direction[1]
    elif q == 0:
        dq = y_direction[0]
    return (dp, dq)

if __name__=="__main__":
    w, h = map(int, input().split()) # 가로(col), 세로(row)
    p, q = map(int, input().split()) # 받은 출발점
    T = int(input())
    t_info = [0]*200000000 #t시간의 위치를 저장한다.
    dp = 1; dq = 1; #default
    for t in range(1,T+1): #1분 뒤부터 들어감
        #t_info[t] = #여기에는 튜플이 원소로 들어감
        if iswall(p,q,w,h):
            dp = turn(p, q, w, h)[0]
            dq = turn(p, q, w, h)[1]
            p += dp
            q += dq
            result = (p,q)
            t_info[t] = result
        else:
            p += dp
            q += dq
            result = (p,q)
            t_info[t] = result
print(t_info[T][0],t_info[T][1] )
