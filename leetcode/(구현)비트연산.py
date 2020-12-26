# n번째 비트 켜기
def nth_bit_on(n):
    return (1<<n)

# n번 비트 켜져있는지 확인
def is_nth_bit_on(num,n):
    return True if num&(1<<n) else False  # num&(1<<n) 나오면 수 자체(n번 비트 켜진 수)가 반환됨

# n개의 비트 모두 켜기
def bit_on_upto_n(n):
    return (1<<n)-1

# 정수의 2의 지수승 여부 판단하기
def is_power_of_2(num):
    return num&(num-1)==0

# 2진수에서 1비트 개수 구하기
def count_bit(num):
    cnt=k=0
    while num>=(1<<k): # 0,1,2... 번째 비트 차례로 1을 확인하겠다.
        if num&(1<<k):
            cnt+=1
        k+=1
    return cnt

# boolean값 toggle하기
def toogle(flag):
    flag ^= True
    return flag

# 비트 연산으로 차집합 구현하기
def differ(num,n):
    return num&~(1<<n)

# 비트 연산으로 수의 뺄셈 구현하기 (차집합과 달리 공집합일때도 수가 변한다. 차집합은 의도적으로 비트 켜진 상태를 끄면서 차집합 구함)
def substract(num,n):
    return num-(1<<n)

print(nth_bit_on(5))
print(bin(nth_bit_on(5)))

print(is_nth_bit_on(32,5))


print(bit_on_upto_n(5))
print(bin(bit_on_upto_n(5)))

print(is_power_of_2(2**10))
print(is_power_of_2(2**10+1))

print(count_bit(5))
print(count_bit(8))

print(toogle(1))
print(toogle(0))

# 1이 켜져있는 n번째 자리수라면 수의 연산이나 집합의 연산이 같다.
print(differ(7,1))
print(substract(7,1))

# 1이 꺼져있는 n번째 자리수라면 수의 연산과 집합 연산이 다르다. 집합의 연산은 결과가 바뀌지 않는다. (공집합 뺐으므로)
print(differ(10,2))
print(substract(10,2))

# 수 이진수표현 집합
#-> 수를 이진수로 바꿔 비트마스킹할 수 있음 (컴퓨터의 연산법)
#-> 이진수로 바꿨다면 집합을 표현하기도 함. 단순히 수로 끝나지 않고.