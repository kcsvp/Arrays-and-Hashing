class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        size = 2**k
        curr = s[:k]
        cache = {curr}
        cnt = 1
        for i in range(k,len(s)):
            curr = curr[1:] + s[i]
            if curr not in cache:
                cache.add(curr)  
                cnt += 1
            if cnt == size:
                return True

        return False