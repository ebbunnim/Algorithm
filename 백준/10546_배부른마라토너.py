
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    start_dict = defaultdict(int)
    for _ in range(N):
        start_dict[input()] += 1
    for _ in range(N-1):
        start_dict[input()]+=1
    for ele in start_dict:
        if start_dict[ele] %2 == 1:
            print(ele)
