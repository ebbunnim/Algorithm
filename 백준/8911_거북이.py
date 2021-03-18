import sys
sys.stdin = open('input.txt','r')

def validate(x,y):
    global lx,rx,ly,ry
    if lx>x:
        lx=x
    if rx<x:
        rx=x
    if ly>y:
        ly=y
    if ry<y:
        ry=y

if __name__ == '__main__':
    T=int(input())
    dx=[-1,0,1,0] # R은,
    dy=[0,1,0,-1]
    for _ in range(T):
        x, y, d = 0, 0, 0
        lx, rx, ly, ry = 0, 0, 0, 0
        rules=input()
        for rule in rules:
            if rule == 'F':
                x += dx[d]
                y += dy[d]
                validate(x, y)
            elif rule == 'B':
                x -= dx[d]
                y -= dy[d]
                validate(x, y)
            elif rule == 'L':
                if d - 1 < 0:
                    d = (d - 1) + 4
                else:
                    d = (d - 1)
            else:  # rule=='R'
                d = (d + 1) %4
        print(abs(rx-lx)*abs(ry-ly))