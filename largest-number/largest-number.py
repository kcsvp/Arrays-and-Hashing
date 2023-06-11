class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = [str(each) for each in nums]
        def compare(x,y):
            return -(int(x+y)- int(y+x))
        nums.sort(key = cmp_to_key(compare))
        sol = ''.join(nums).lstrip('0')
        if sol == '':
            return '0'
        return sol
