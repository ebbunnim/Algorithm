import heapq

def solution(operations):
    heap = []
    for i in range(len(operations)):
        way, val = operations[i].split()
        if way =='I':
            heapq.heappush(heap, int(val))
        else:
            if heap!=[]:
                if val == '-1': # 최솟값 삭제
                    heapq.heappop(heap)
                else: # 최댓값 삭제
                    heap.pop(heap.index(heapq.nlargest(1, heap)[0])) # heap에서 큰순으로 1개 원소 가져와
    if heap==[]:
        return [0,0]
    else:
        return [heapq.nlargest(1, heap)[0], heapq.nsmallest(1, heap)[0]]