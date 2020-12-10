import sys
sys.stdin = open('input.txt','r')


# 반드시 횟수만큼 바꿔야 한다는 제약이 있다는 것에 주의.
if __name__=="__main__":
    for t in range(int(input())):
        num, chance = input().split()
        chance = int(chance)
        num = list(num)
        maxv = 0
        cnt = 0
        def dfs(start,num):
            global maxv, cnt

            if cnt==chance:
                maxv = max(maxv, int(''.join(num)))
                return

            for l in range(start,len(num)):
                for r in range(l+1,len(num)):
                    if num[l]<=num[r]: # 동일값도 swap한다.
                        num[l],num[r]=num[r],num[l]
                        cnt+=1
                        dfs(l,num)
                        num[l],num[r]=num[r],num[l]
                        cnt-=1

        dfs(0,num) # start는 중복 방지를 위해서. 이전꺼는 순회하지 마 - vis 관리하지 않고

        # chance 다 안쓰면 (모두 감소하는 수로 이뤄진 경우도 이 경우로 됨. 최대한 바꿔도 찬스가 남은 경우도)
        if maxv==0:
            left_chance = chance-cnt
            if left_chance%2:
                num[-2],num[-1]=num[-1],num[-2]
            maxv = int(''.join(num))

        print(f'#{t+1} {maxv}')

