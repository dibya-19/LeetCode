class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        max_total = nums[0]
        for i in range(n):
            total += nums[i]
            max_total = max(max_total,total)
            if total < 0:
                total = 0
                
        return max_total

        