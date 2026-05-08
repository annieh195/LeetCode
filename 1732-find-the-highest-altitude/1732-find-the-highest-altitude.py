class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        alt = 0
        for i in range(len(gain)):
            alt += gain[i]
            maxx = max(maxx, alt)
        return maxx