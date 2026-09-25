import math
class Solution:

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 0, piles[-1]-1
        rate = piles[-1]
        

        # rate has to be between 1 and max(piles)
        # start at midpoint: eg: 1 2 3 4, start at 2
        # if 2 satisfies, then decrease rate by 1 - if decreased rate does not satisfy h then exit

        if h == len(piles):
            return piles[-1]
        
        while l <= r:
            eatingRate = l + ((r-l)//2)
            time = 0
            sumofPiles = 0
            for pile in piles:
                time += math.ceil(pile/eatingRate)
                sumofPiles += pile
            if sumofPiles <= h:
                return 1
            elif time <= h and eatingRate < rate:
                rate = eatingRate
                r = eatingRate - 1 # moving midpoint to lower half of range
            else:
                l = eatingRate + 1 # need to increase midpoint to upper half of range
        return rate
            





        