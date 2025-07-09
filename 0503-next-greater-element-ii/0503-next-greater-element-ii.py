class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        new_nums = nums + nums + [inf]
        res = [-1]*len(nums)
        st = []

        for i in range(len(new_nums)):
            while st and new_nums[st[-1]] < new_nums[i]:
                j = st.pop()
                if j < len(nums) and new_nums[i] != inf:
                    res[j] = new_nums[i]
            st.append(i)
        return res