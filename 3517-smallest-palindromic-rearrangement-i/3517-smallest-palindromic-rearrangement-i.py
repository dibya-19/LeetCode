class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        half = n // 2
        left = sorted(s[:half])
        if n % 2:
            return "".join(left) + s[half] + "".join(left[::-1])
        else:
            return "".join(left) + "".join(left[::-1]) 