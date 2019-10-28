#가장 많이 꼬리를 물리게 해야
#2개씩 짝지어서 이어져야

def my_train(x):
    l=[]
    for i in range(len(x)//2):
        result=[]
        for j in range(2):
            result.append(x[j+2*i])
        l.append(result)
    return l



def pair(a): #a는 이차배열 받아야
    for i in range(len(l)):
        minIndex = i
        for j in range(len(l)-1):
            if a[minIndex][1] == a[i+j][0]:
                a[minIndex] += a[i]
                minIndex = i+1

    return a[minIndex]


N = int(input())
num = list(map(int, input().split()))
my_list=[]


for element in num:
    temp = num.count(element)
    Index = num.index(element)
    l = my_train(num)

    if temp == 1:
        if Index%2:
            end = element #가장 끝으로
        if not Index%2:
            start = element

for k in range(len(l)):
    for h in range(2):
        if l[k][h] == start:
            l[0] = l[k]

        if l[k][h] == end:
            l[-1] = l[k]

print(pair(l))



#print(num)
#
#print(my_train([1,2,5,1,2,4,4,3]))
