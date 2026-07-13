class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        m = len(s)
        n = len(g)
        l,r = 0,0
        while l < m and r < n:
            if s[l] >= g[r]:
                r += 1

            l += 1

        return r
