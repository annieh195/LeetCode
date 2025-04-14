class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(cap):
            count = 1
            trip = 0
            for weight in weights:
                if trip + weight <= cap: 
                    trip += weight
                else:
                    trip = weight
                    count += 1
            return count <= days

        l = max(weights)
        r = sum(weights)
        while l <= r:
            mid = (l+r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l