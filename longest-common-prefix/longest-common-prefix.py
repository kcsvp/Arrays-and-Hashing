class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str , min_len = None,math.inf
        for each in strs:
            if len(each) < min_len:
                min_str = each
                min_len = len(each)

        sol = min_len

        for i in range(len(strs)):
            if min_str == strs[i]:
                continue
            j = 0
            while j < min_len:
                if min_str[j] != strs[i][j]:
                    break
                j += 1
            if j < sol:
                sol = j

        return min_str[:sol]