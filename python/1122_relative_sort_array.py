from icecream import ic

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        output = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    output.append(j)
        for i in sorted(arr1):
            if i not in arr2:
                output.append(i)
        return output
    
sol = Solution()
sol.relativeSortArray(arr1=[2,3,1,3,2,4,6,7,9,2,19], arr2=[2,1,4,3,9,6])
ic(sol.relativeSortArray(arr1=[2,3,1,3,2,4,6,7,9,2,19], arr2=[2,1,4,3,9,6]))