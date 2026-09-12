class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = set()
        length = 0
        j = 0

        for i in range(len(s)):
            while s[i] in hSet:
                hSet.remove(s[j])
                j += 1
            hSet.add(s[i])
            curr = i - j + 1
            length = max(curr, length)
        return length 



