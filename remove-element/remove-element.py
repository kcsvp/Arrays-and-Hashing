class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # queue = []
        # n = len(nums)
        # for p in range(len(nums)):
        #     if nums[p] == val:
        #         queue.append(p)
        #         n -= 1
        #     elif queue != []:
        #         index = queue.pop(0)
        #         nums[index] = nums[p]
        #         queue.append(p)        
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
