class Solution:

    def fib(self, N: int) -> int:  # F(N)을 구해라

        # pythonic
        x, y = 0, 1
        for _ in range(N):
            x, y = y, x + y
        return x

#         타뷸레이션 bottom -> top : 32ms
#         if N<=1:
#             return N
#         D =[0]*(1+N)
#         D[0]=0
#         D[1]=1
#         for i in range(2, N+1):
#             D[i] = D[i-1]+D[i-2]
#         return D[N]


#         메모이제이션 top -> bottom
#         if N<=1:
#             return N
#         if self.D[N]:
#             return self.D[N]
#         self.D[N] = self.fib(N-1)+self.fib(N-2)
#         return self.D[N]


#         recursion : 1000ms
#         if N==0:
#             return 0
#         if N==1:
#             return 1
#         return self.fib(N-1)+self.fib(N-2)



