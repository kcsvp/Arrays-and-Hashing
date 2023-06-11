class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        for each in t:
            if i < len(s):
                if each == s[i]:
                    i += 1
            else:
                break
                
        
        return True if i == len(s) else False

        