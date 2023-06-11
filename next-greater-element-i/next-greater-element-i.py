class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # mapping_sol = [nums2.index(each) for each in nums1]
        # for i in range(len(nums1)):
        #     k = mapping_sol[i]
        #     mapping_sol[i] = -1
        #     for j in range(k+1,len(nums2)):
        #         if nums2[j]>nums1[i]:
        #             mapping_sol[i] = nums2[j]
        #             break
        # return mapping_sol

        mapping = {each:i for i,each in enumerate(nums2)}
        sol = [-1]*len(nums1)
        for i,each in enumerate(nums1):
            for j in range(mapping[each] + 1,len(nums2)):
                if nums2[j] > each:
                    sol[i] = nums2[j]
                    break
            
        return sol