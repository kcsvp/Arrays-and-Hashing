class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        cache = dict()
        total = 0

        for i,each in enumerate(nums):
            total += each
            rem = total%k
            if i>0 and rem==0:
                return True
            if rem in cache:
                index = cache[rem]
                if i-index > 1:
                    print(i,index)
                    return True
                continue
            cache[rem] = i
        

        return False
            