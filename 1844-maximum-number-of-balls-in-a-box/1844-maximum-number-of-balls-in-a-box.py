class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        mp = defaultdict(int)

        for num in range(lowLimit, highLimit+1):
            summ = 0
            for digit in str(num):
                summ += int(digit)
            mp[summ] += 1
        return max(mp.values())