class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        mod = 10**9 + 7
        nums1s = sorted(nums1)
        s = sum([abs(a - b) for a, b in zip(nums1, nums2)])
        res = s

        for i in range(len(nums2)):
            idx = bisect_right(nums1s, nums2[i])
            diff1 = diff2 = inf
            if idx < len(nums1s):
                diff1 = abs(nums1s[idx] - nums2[i])
            if idx-1 >= 0:
                diff2 = abs(nums1s[idx-1] - nums2[i])

            curdiff = abs(nums1[i] - nums2[i])
            bestdiff = min(diff1, diff2)
            res = min(res, s - curdiff + bestdiff)
        return res % mod

