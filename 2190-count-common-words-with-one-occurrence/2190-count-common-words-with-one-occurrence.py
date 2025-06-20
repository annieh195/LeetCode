class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        mp = defaultdict(int)
        res = 0

        for word in words1:
            mp[word] += 1

        for word in words2:
            mp[word] += 1

        for word in words2:
            if word in words1 and mp[word] == 2:
                res += 1
        return res