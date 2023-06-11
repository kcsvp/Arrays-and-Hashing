class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ref = Counter(p)
        cache = dict()
        sol = []
        for i,c in enumerate(s):
            if i >= len(p):
                cache[s[i-len(p)]] -= 1
                if cache[s[i-len(p)]] == 0:
                    cache.pop(s[i-len(p)])
            cache[c] = cache.get(c,0) + 1
            if cache == ref:
                sol.append(i-len(p) + 1)
            

        return sol
        