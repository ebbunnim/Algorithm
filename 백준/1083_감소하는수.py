import sys
sys.stdin = open('input.txt','r')

# n으로 몇번째 군의 몇번째? 이걸 판단하느냐 vs 다 만들어놓고 n을 찝어서 반환하느냐. 여기선 후자를 선택

if __name__ == '__main__':
    N = int(input())

    def dfs(startidx, cnt,res,Nlist):
        global idx
        if cnt == s: # 자리수를 다 채웠다.
            tmp=''
            for r in res:
                tmp+=str(r)
            ans.append(int(tmp))
            idx += 1
            return

        for i in range(startidx,len(Nlist)):
            res.append(Nlist[i])
            cnt += 1
            dfs(i+1,cnt,res,Nlist)
            cnt-= 1
            res.pop()


    if N>=1023:  # N 은 인덱스 개념임에 주의
        print(-1)
    else:
        idx = 0
        ans = []
        for s in range(1,11): # 만들 숫자의 자리수. 1000000번째 물으면 몇번째 자리까지 가야하는지? 찍어봐 (주의)
            for start in range(s-1,10): # s-1~9까지가 만들 숫자의 맨 앞자리 숫자
                res = []
                res.append(start)
                if s == 1:
                    ans.append(start)
                    idx+=1
                    continue
                else: # 두 자리 이상의 숫자
                    Nlist = [i for i in range(start-1,-1,-1)]
                    dfs(0,1,res, Nlist)
                    if idx > N+1 :
                        break
        ans.sort() # 주의. Nlist를 reverse하게 만들었기 때문에 큰 수부터 만들어지지만, 'i번째'를 구할때는 작은 수 부터 카운팅됨
        print(ans[N])
