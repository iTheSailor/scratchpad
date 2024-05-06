from icecream import ic

class Solution(object):
    def __init__(self):
        self.m=float('-inf')
    def maxArea(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        a = 0
        b = len(h)-1
        while a < b:
            i = min(h[a], h[b])
            n = len(h)-1
            v = i*(b-a)
            sol.maxHolder(v)
            ic(i, n, v, h, h[a], h[b], self.m)
            if h[a] > h[b]:
                b-=1
            else:
                a+=1
        ic(self.m)
        return int(self.m)
    
    def maxHolder(self, v):   
        if v>self.m:
            self.m=v




        







height=[1,8,6,2,5,4,8,3,7]
sol = Solution()
sol.maxArea(height)