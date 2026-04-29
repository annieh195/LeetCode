class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        mp = defaultdict(int)
        for num in arr:
            mp[num] += 1
        
        return max(mp, key=mp.get)