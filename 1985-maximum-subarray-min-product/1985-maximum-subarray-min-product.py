class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        modulo = 10**9 + 7
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[i] + nums[i])

        nums.append(-inf)
        st = []
        ma = 0
        for i in range(len(nums)):
            while st and nums[st[-1]] > nums[i]:
                j = st.pop()
                L = (st[-1] if st else -1) + 1
                R = i-1
                summ = prefix[R+1] - prefix[L]
                ma = max(ma, summ*nums[j])
            st.append(i)
        return ma % modulo