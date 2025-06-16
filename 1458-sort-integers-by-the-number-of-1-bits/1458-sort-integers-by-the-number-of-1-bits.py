class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        mp = defaultdict(list)
        res = []
        for num in arr:
            mp[bin(num).count('1')].append(num)
        
        for key in sorted(mp):
            res += sorted(mp[key])
        return res

            
