import sys
sys.stdin = open('input.txt','r')

from collections import Counter

if __name__ == '__main__':
    S = list(input())
    # 최소한의 횟수로 뒤집고, 하나의  수로 다 맞춰라
    # 연속된 하나 이상의 수를 잡고 다 뒤집는다.
    # 덩이리씩 뒤집는..? => 근데, 전체 다 뒤집고 중복해서 다시 뒤집을 수

    # 중복을 제거할거고, -> 방향으로 구간 당
    # 만약에 얘네들이 다 똑같으면 그 때는 한번만 뒤집으면 돼
    # 아니면, 구간으로 나뉜 갯수만 카운트하면 된다.
    convert_to_1=0
    convert_to_0=0

    for i in range(1,len(S)):
        # 뒤를 돌아보다가, 다르다고 하면, 왼쪽에 있는 애를 넣을 것. 마지막에는 처리해주고
        if S[i]!=S[i-1]:
            if S[i-1]=='0':
                convert_to_1+=1
            else:
                convert_to_0+=1
    if S[-1]=='0':
        convert_to_1+=1
    else:
        convert_to_0+=1
    print(min(convert_to_0,convert_to_1))

