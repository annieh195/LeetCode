class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        mp = defaultdict(int)
        
        for card in deck:
            mp[card] += 1
        
        mpvalues = list(mp.values())
        g = mpvalues[0]
        for value in mpvalues:
            g = gcd(g, value)

        if g == 1:
            return False
        return True

        