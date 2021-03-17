import sys
sys.stdin = open('input.txt','r')

# 세로 기준으로 문자를 더함. 가로는 크기 3까지
# 근데, 1이 문제임. 세로 기준으로 다 갔는데 비어있으면 바로 타 (4와 비교해서 구현할 것). 원래는 하나 # 잡히면 3개씩 가로 윈도우를 잡는데 1만 제외함

num_dict={
    '######...######':0,
    '#####.....':1,
    '#.####.#.####.#':2,
    '#.#.##.#.######':3,
    '###....#..#####':4,
    '###.##.#.##.###':5,
    '######.#.##.###':6,
    '#....#....#####':7,
    '######.#.######':8,
    '###.##.#.######':9
}

def check(i):
    res=''
    for c in range(i,i+3):
        for i in range(5):
            res+=s[c+w*i]
    if res[5:10]=='.....': # 더 보면 혼란스러울 수 있음
        return 1
    return num_dict[res]


if __name__ == '__main__':
    n=int(input())
    s=input()
    w,h=n//5,5
    i=0
    while i<w:# 맨 윗 줄에서 판별
        if i==w-1:
            res=''
            for j in range(5):
                res+=s[i+w*j]
            if res=='#####':
                print(1,end='')
            break
        if s[i]=='#':
            res=check(i)
            print(res,end='')
            if res==1:
                i+=2
            else:
                i+=3
        else:
            i+=1
# 1이 문제, 1이 우측 극단에 있을 수도 있다.