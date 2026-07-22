class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        for i in range(len(nums)):
            sq = nums[i] ** 2
            arr.append(sq)

        arr.sort()
        return arr
        