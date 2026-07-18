class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        eq = int(bin(n)[2:])
        digit = 0
        count = 0
        while eq != 0:
            digit = eq % 10
            if digit == 1:
                count += 1
            eq //= 10

        return count
        