class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1,-1,-1):
            if res > 0 and s[i] == ' ':
                break
            elif s[i] == ' ':
                continue
            res += 1
        
        return res
        # res = 0
        # for each in s[::-1]:
        #     if res > 0 and each == ' ':
        #         break
        #     elif each == ' ':
        #         continue
        #     res += 1
        # return res
        