class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        total1 = sum(nums1)
        total2 = sum(nums2)
        zero1 = Counter(nums1)[0]
        zero2 = Counter(nums2)[0]

        if ((zero1== 0 and zero2==0) and (total1 != total2)) or (zero1==0 and total1-total2<zero2) or (zero2==0 and total2-total1<zero1):
            return -1
        return max(total1+zero1, total2+zero2)
