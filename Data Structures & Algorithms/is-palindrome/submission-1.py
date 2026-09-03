class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        for c in s:
            code = ord(c)
            if not (
                ord('A') <= code <= ord('Z') or      # 0–9
                ord('a') <= code <= ord('z') or      # A–Z
                ord('0') <= code <= ord('9')        # a–z
            ):
                s = s.replace(c, "")
        
        s = s.lower()

        l, r = 0, len(s) - 1

        while l < r:
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 
                
        