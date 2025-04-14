class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(maxtime):
            total = 0
            for t in time:
                total += maxtime // t
            return total >= totalTrips

        l = 1
        r = min(time) * totalTrips
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
