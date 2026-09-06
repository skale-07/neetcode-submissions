class Solution:
    def isPalindrome(self, s: str) -> bool:
        output = []
        for c in s:
            if (
                ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9')
            ):
                output.append(c.lower())

        s = "".join(output)

        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True 


