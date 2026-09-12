class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = set()
        l = 0
        longLen = 0

        for r in range(len(s)):
            while s[r] in hSet:
                hSet.remove(s[l])
                l += 1
            hSet.add(s[r])
            longLen = max(longLen, len(s[l:r]) + 1)
        return longLen 