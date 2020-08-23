
def cal(mylist):
    length = len(mylist)
    ans = 0
    if length%2 == 0:
        for i in range(0,length,2):
            ans += mylist[i]*mylist[i+1]
    else:
        for i in range(0,length-1,2):
            ans += mylist[i]*mylist[i+1]
        ans += mylist[length-1]
    return ans

if __name__ == '__main__':
    N = int(input())
    minus, plus = [], []
    for i in range(N):
        tmp = int(input())
        if tmp <= 0: # 0을 minus 배열에 추가!
            minus.append(tmp)
        else:
            plus.append(tmp)

    minus.sort()

    plus.sort(reverse=True)
    ans = 0
    while plus and plus[-1] == 1:
        ans += plus.pop()

    ans += cal(minus)
    ans += cal(plus)
    print(ans)