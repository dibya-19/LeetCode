class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_index = [-1]*255
        n = len(s)
        l=0
        r=0
        max_len = 0

        for r in range(len(s)):
            ch = ord(s[r])

            if last_index[ch] >= l:
                l = last_index[ch] + 1

            max_len = max(max_len,r-l+1)
            last_index[ch] = r
        return max_len

        