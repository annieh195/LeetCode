class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stk and temperatures[stk[-1]] < temp:
                idx = stk.pop()
                ans[idx] = i - idx
            stk.append(i)
        return ans