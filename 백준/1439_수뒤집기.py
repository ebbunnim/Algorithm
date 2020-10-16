import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    S = list(input())
    convert_to_1=0
    convert_to_0=0

    for i in range(1,len(S)):
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

