class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = bin(n)[2:].zfill(32)
        a = a[::-1]
        ans = "".join(a)
        res = int(ans,2)
        return res