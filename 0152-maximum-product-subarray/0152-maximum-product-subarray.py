class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = res = nums[0]
        for num in nums[1:]:
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            curr_max = max(curr_max * num, num)
            curr_min = min(curr_min * num, num)
            res = max(res,curr_max)
        return res 