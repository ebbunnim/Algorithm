import sys
sys.stdin = open("input.txt", "r")

# 문자를 숫자로 만드는 방법



if __name__ == "__main__":
    T = 10
    for tc in range(1, T+1):
        N = int(input())
        l = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(8):
            string = input() # 띄어쓰기 제거한 리스트를 다시 string으로 받음 유의, 띄어쓰기 어떻게 처리?
            l[i] = string  # string을 각 idx에 넣음

        # 만약에 N=4라면, 8-4+1
        cnt = 0
        # 여기서 시작점이 처음부터 안돌음.
        for j in range(8):
            for i in range(8 - N + 1):
                temp = l[j][i:i + N]
                if temp == temp[::-1]:
                    cnt += 1

        temp = ''
        for i in range(8):
            for j in range(8-N+1):  # 슬라이싱횟수
                temp = ''
                for k in range(N):
                    temp += l[j+k][i]
                if temp == temp[::-1]:
                    cnt += 1

        print('#%d %d' % (tc,cnt))