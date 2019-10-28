#각 행, 열마다 브루스포스 알고리즘을 구현해야
#cont를 입력받고 그만큼씩 탐색, 그게 회문이냐를 검사하는 것 -> 맞다면 1씩 전역으로 더해줌
#인덱스적 접근



def pal_count(par_len, string): #한줄씩 사용하는 함수
    cnt=0
    for i in range(len(string)//2+1): ####주의!!! +1!!
        if string[i] == string[par_len-1+i] and string[i+1] == string[par_len-2+i]:
            cnt+=1
    return cnt


par_len = int(input())
l = []
for i in range(8):
    l.append(list(input().split()))

cnt=0; temp=[]; result=0
for row in range(8):
    result += pal_count(par_len, l[row])
    for col in range(8):
        temp.append(l[col][row])
        result += pal_count(par_len, temp)


print(result)




