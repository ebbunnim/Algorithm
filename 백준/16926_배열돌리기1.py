import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,M,R=map(int,input().split())
    corners=[(0,0)]