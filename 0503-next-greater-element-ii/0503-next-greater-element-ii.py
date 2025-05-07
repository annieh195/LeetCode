class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        newnums = nums + nums + [inf]
        st = []
        res = [-1] * len(nums)

        for i in range(len(newnums)):
            while st and newnums[st[-1]] < newnums[i]:
                j = st.pop()
                if j < len(nums) and newnums[i] != inf:
                    res[j] = newnums[i]
            st.append(i)
        return res