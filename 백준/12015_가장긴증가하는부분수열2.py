
def binary(A, target):
    start = 0
    end = len(A)-1

    while start < end: # 새로운 수가 삽입되므로, 원래의 이분탐색과 다르게 mid==target일수는 없다.
        mid = (start + end)//2
        if A[mid] < target:
            start = mid+1
        else:
            end = mid # 원래는 mid-1로 줄이는데, end 자리를 target으로 갱신하기 때문에 mid로
    return end

if __name__ == '__main__':

    n = int(input())
    n_list = [0] + list(map(int, input().split()))

    A = [0]

    for i in range(1, n+1):
        if A[-1] < n_list[i]:
            A.append(n_list[i])
        else:
            # binary
            A[binary(A, n_list[i])] = n_list[i] # 작은 값이 나오면 갱신한다.
    print(len(A)-1)
