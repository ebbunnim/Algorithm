import sys
sys.stdin = open('input.txt','r')

#  1, 2, 3으로만 이루어져 있는 길이가 N인 좋은 수열들 중에서 가장 작은 수를 나타내는 수열
# 좋은 수열 : 인접하게 같은 수이면 안됨, 1 1 은 물론 12 12 도
if __name__ == '__main__':
    N = int(input())

    def check(l,s): # 새로 추가된 원소에서 시작해, 1~1//2+1 크기로 슬라이싱된 부분이 같은지 확인
        for c in range(1,l//2+1): # 수열을 쪼개는 길이
            A = s[l-c:]
            B = s[l-2*c:l-c]
            if int(A)==int(B):
                return False
        return True

    # make sequence
    D = ['1','2','3']
    def dfs(l,res):
        if not check(l,res):
            return

        if l == N:
            print(res)
            exit()

        for d in D:
            dfs(l+1,res+d)

    dfs(0,'')



