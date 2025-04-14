class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def check(tastiness):
            prev = price[0]
            count = 1
            for i in range(1, len(price)):
                if price[i] - prev >= tastiness:
                    count += 1
                    prev = price[i]
            return count >= k
        
        price.sort()
        l = 0
        r = price[-1] - price[0]
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r