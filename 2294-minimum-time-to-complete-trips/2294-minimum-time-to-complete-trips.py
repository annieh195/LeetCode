class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(maxtime):
            count = []
            for i in range(len(time)):
                count.append(maxtime // time[i])
            return sum(count) >= totalTrips 

        l = min(time)
        r = 10**15
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
