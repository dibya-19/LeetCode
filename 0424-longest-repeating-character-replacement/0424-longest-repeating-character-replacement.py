class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        max_freq = 0
        left = 0
        res = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0) + 1
            max_freq = max(max_freq,freq[s[right]])
            if (right-left+1 - max_freq) > k:
                freq[s[left]] -= 1
                left += 1

            res = max(res,right-left+1)

        return res