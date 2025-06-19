class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        mp = defaultdict(int)
        count = 0
        for s in arr:
            mp[s] += 1

        for s in arr:
            if mp[s] == 1:
                count += 1
                if count == k:
                    return s
        return ""