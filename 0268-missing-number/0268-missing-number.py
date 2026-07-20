class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        suma = (n*(n+1))//2

        return suma-sum(nums)
        