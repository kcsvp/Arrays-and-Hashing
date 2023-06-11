class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cache = dict()
        for row in wall:
            curr = 0
            for each in row:
                curr += each
                cache[curr] = cache.get(curr,0) + 1

        cache.pop(curr)
        
        if not cache:
            return len(wall)

        return len(wall) - cache[max(cache,key = cache.get)]