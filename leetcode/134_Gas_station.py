class Solution:
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