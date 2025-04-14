class Solution:
    def mySqrt(self, x: int) -> int:
        def check(num):
            if num * num <= x:
                return True
            return False

        l = 0
        r = x
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r