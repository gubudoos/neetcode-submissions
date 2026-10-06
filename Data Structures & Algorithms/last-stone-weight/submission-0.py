class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        heapq.heapify(res)
        for stone in stones:
            heapq.heappush(res, -stone)
        
        while len(res) > 1:
            largest = -(heapq.heappop(res))
            next_largest = -(heapq.heappop(res))
            diff = largest - next_largest
            if diff > 0:
                heapq.heappush(res, -diff)
        
        return -res[0] if res else 0


        