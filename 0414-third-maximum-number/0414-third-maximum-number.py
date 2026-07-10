class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distinct = sorted(set(nums),reverse=True)
        if (len(distinct)>=3):
            return distinct[2]

        else:
            return max(distinct)

        
        