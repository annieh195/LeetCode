class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = (s1+ " " +s2).split()
        mp = defaultdict(int)
        res = []

        for word in s:
            mp[word] += 1
        
        for key, value in mp.items():
            if value == 1:
                res.append(key)
        return res

                
