import sys
sys.stdin = open('input.txt','r')

def check(bit,num):
    return 1 if bit&(1<<num) else 0

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    bit=0
    for _ in range(N):
        order = list(sys.stdin.readline().split())
        if order[0][0]=='a' and order[0][1]=='l':
            bit = (1 << 20) - 1
        elif order[0][0]=='e':
            bit = 0
        elif order[0][0]=='a' and order[0][1]=='d':
            bit |= (1 << int(order[1])-1)
        elif order[0][0]=='r':
            bit &= ~(1 << int(order[1])-1)
        elif order[0][0]=='c':
            print(check(bit,int(order[1])-1))
        elif order[0][0]=='t':
            bit ^= (1 << int(order[1])-1)

