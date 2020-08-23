from itertools import permutations

if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int, input().split()))
    perms = list(permutations(N_list,N))
    max = 0
    for perm in perms:
        res =0
        for i in range(1,N):
            res += abs(perm[i]-perm[i-1])
        if res > max:
            max = res
    print(max)
