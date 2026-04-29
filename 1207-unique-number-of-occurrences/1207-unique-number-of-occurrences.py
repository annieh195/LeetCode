class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mp = defaultdict(int)

        for num in arr:
            mp[num] += 1
        
        check = set()
        
        for v in mp.values():
            if v in check:
                return False
            else:
                check.add(v)
        return True