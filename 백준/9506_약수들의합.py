import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')



if __name__ == '__main__':
    while True:

        N =int(input())
        if N == -1:
            break

        nums = [i for i in range(1,N+1) if N%i==0]
        nums.sort()
        if sum(nums[:-1])==N:
            nums.sort()
            print(str(N) + ' = ', end='')
            for i in range(len(nums)-1):
                if i == len(nums)-2:
                    print(nums[i])
                    break
                print(str(nums[i])+' + ', end='')
        else:
            print(f'{N} is NOT perfect.')

