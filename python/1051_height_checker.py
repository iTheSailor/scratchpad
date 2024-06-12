from icecream import ic

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights2 = sorted(heights)
        output = 0
        for i in range(len(heights)):
            if heights[i] != heights2[i]:
                output += 1
        return output
        

sol = Solution()
sol.heightChecker(heights=[1,1,4,2,1,3])
ic(sol.heightChecker(heights=[1,1,4,2,1,3]))