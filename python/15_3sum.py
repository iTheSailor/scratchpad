from icecream import ic
class Solution(object):
    def threeSum(self, nums):
        nums.sort()  
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  
            
            left, right = i + 1, n - 1  
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1  
                else:
                    right -= 1  
        
        return result


nums1 = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 1, 1]
nums3 = [0, 0, 0]

sol=Solution()
ic(sol.threeSum(nums1))
ic(sol.threeSum(nums2))
ic(sol.threeSum(nums3))





            
