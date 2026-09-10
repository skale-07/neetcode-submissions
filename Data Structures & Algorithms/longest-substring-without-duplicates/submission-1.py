class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in hSet:
                hSet.remove(s[l])
                l += 1
            hSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    




            


        