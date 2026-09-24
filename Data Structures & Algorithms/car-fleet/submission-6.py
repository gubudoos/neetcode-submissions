class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort cars in order of highest position to lowest position
        # traverse in reverse order of position

        key = [[p,s] for p,s in zip(position,speed)]
        stack = []
        # print(sorted(key))

        for p,s in sorted(key)[::-1]:
            # print(stack)
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)


        