class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)

        for num in nums:
            mp[num] += 1
        
        if max(mp.values()) >= 2:
            return True
        return False