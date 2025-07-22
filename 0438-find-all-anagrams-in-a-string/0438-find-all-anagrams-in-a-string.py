class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        window = defaultdict(int)
        mp_p = defaultdict(int)
        l = 0
        res = []
        
        for i in range(len(p)):
            mp_p[p[i]] += 1

        for r in range(len(s)):
            window[s[r]] += 1
            while r-l+1 > len(p):
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1

            if window == mp_p:
                res.append(l)
        return res