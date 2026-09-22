class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0

        # [2, 3, 1, 3] = 2+2 = 4

        l, r = 0, len(height)-1
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

        





            

        
        