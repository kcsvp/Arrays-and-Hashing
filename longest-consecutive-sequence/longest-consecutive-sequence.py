class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        t = len(nums)
        nums = set(nums)
        sol = 1
        i = 0
        for each in nums:
            left,right = 0,0
            for i in range(1,i + 1):
                if (each-i) not in nums:
                    break
                left = i
            for i in range(1,t-i+1):
                if (each+i) not in nums:
                    break
                right = i
            sol = max(sol,left + right + 1)
            if sol == t:
                return t
            i += 1
        return sol

       