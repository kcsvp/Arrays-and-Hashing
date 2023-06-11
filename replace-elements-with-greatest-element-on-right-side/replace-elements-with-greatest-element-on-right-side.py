class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        i = len(arr)-1
        mx_num = -1

        while i>=0:
            temp = arr[i]
            arr[i] = mx_num
            mx_num = max(temp,mx_num)
            i -= 1

        return arr