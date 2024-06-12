from icecream import ic

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = float('inf')
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closest - target):
                    closest = s
                if s < target:
                    l += 1
                else:
                    r -= 1
        return closest