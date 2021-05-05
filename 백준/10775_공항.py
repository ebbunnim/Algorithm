import sys
sys.stdin = open('input.txt','r')

def find(n):
    if gates[n] == n:
        return n
    else:
        gates[n] = find(gates[n])
        return gates[n]


def union(a, b):
    x = find(a)
    y = find(b)
    gates[x] = y
    return

if __name__ == "__main__":
    numGate = int(input())
    numPlane = int(input())
    gates = list(range(numGate + 1))

    cnt = 0
    for _ in range(numPlane):
        gate = int(input())
        parent = find(gate)
        if parent == 0:
            break
        union(parent, parent-1)
        cnt += 1
    print(cnt)