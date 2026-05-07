class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx = 0
        for account in accounts:
            maxx = max(maxx, sum(account))
        return maxx