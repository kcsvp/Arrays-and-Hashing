class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cache = set()
        curr = s[:10]
        cache.add(curr)
        sol = set()
        for i in range(10,len(s)):
            curr = curr[1:] + s[i]
            if curr in cache:
                sol.add(curr)
            else:
                cache.add(curr)
        return list(sol)