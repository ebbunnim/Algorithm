import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    S = list(map(int, input()))
    s, e = 0, len(S)-1
    left=right=0
    while s<e:
        left+=S[s]
        right+=S[e]
        s+=1
        e -= 1
    if left == right:
        print('LUCKY')
    else:
        print('READY')

