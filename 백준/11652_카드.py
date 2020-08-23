from collections import defaultdict
import sys

if __name__ == '__main__':
    N = int(input())
    N_dict = defaultdict(int)
    for i in range(N):
        N_dict[int(sys.stdin.readline())] += 1
    max_val = max(list(N_dict.values()))
    ans = pow(2, 62)
    for key, value in N_dict.items():
        if value == max_val and ans > key:
            ans = key
    print(ans)
