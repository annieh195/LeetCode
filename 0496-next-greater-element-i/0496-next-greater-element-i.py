class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mp = defaultdict(int)
        for num in nums2:
            while stack and num > stack[-1]:
                mp[stack.pop()] = num
            stack.append(num)
    
        while stack:
            mp[stack.pop()] = -1

        for i in range(len(nums1)):
            nums1[i] = mp[nums1[i]]
        return nums1