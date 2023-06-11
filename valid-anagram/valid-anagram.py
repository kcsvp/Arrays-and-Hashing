class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for each in set(s):
            if s.count(each) != t.count(each):
                return False
        return True
        
        