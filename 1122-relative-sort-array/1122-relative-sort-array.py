class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        remain = []
        mp = defaultdict(int)
        res = []

        for num in arr2:
            mp[num] = 0
        
        for num in arr1:
            if num in arr2:
                mp[num] += 1
            else:
                remain.append(num)
        
        remain.sort()

        for num in arr2: 
            res.extend([num] * mp[num])
        res.extend(remain)
        return res