#못풀었음
import sys
sys.stdin = open("input1.txt","r")

w, h = map(int, input().split()) #길이이므로 range()에서는 +1씩 해줘야
p, q = map(int, input().split()) #start지점
T = int(input())

#arr를 만든다.
l = [[0]*w for _ in range(h)]

end_x = p+1 #한번 출발했다고 가정
end_y = q+1

for t in range(1, T):
    # ->5, 6, 5, 4, 3, 2, 1, 0 , 1, 2, 3, 4, 5, 6, 5, 4, 3,  ...
    if end_x > w:
        end_x -= 2
        if end_x >= 0:
            end_x -= 1
            continue
        #방향을 바꾼 규칙을 그대로 적용해야 한다.
    elif end_x < 0:
        end_x += 2
        if end_x >= 0:
            end_x -= 1
            continue
    print('x',end_x)

    end_y += 1
    if end_y > h:
        end_y -= 2
    elif end_y < 0:
        end_y += 2
    print('y',end_y)
print(end_x, end_y)





