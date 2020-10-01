class Solution:
    # 반드시 가능한 출발점이 하나이다.
    # 만약, oil<0이라면 i 이전까지의 모든 인덱스는 출발점이 될 수 없다.
    # i 순간에 누적된 gas를 다 까먹을 cost가 존재했다는 의미이므로, i 이전의 어떤 subsum도 현재보단 더 작을 것이므로 다 손실된다는 의미
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1

        oil = 0
        start = 0
        for i in range(len(gas)):
            oil += (gas[i]-cost[i])
            if oil < 0:
                start = i + 1
                oil = 0
        return start

    # 최적화 전 코드
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     for i in range(len(gas)): # start pivot
    #         start = i
    #         oil = 0
    #         flag = 0
    #         for j in range(len(gas)):
    #             idx = (i+j)%len(gas) # 원형 사이클 모듈 연산
    #             oil += (gas[idx]-cost[idx])
    #             if oil < 0:
    #                 flag =1
    #                 break
    #         if flag == 0:
    #             return start
    #     return -1