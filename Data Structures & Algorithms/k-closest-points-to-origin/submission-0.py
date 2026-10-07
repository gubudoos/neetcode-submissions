class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        heapq.heapify(dis)
        for pairs in points:
            x, y = pairs[0], pairs[1]
            euc = ( (x)**2 + (y)**2 )**0.5
            heapq.heappush(dis, (euc, (pairs)))
        # print(dis)
        # print(dis[0][1])
        
        res = []
        while len(res) < k:
            smallest = heapq.heappop(dis)[1]
            res.append(smallest)

        return res