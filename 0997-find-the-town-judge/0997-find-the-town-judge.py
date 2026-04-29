class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = [0] * (n + 1)

        for a, b in trust:
            mp[a] -= 1
            mp[b] += 1

        for person in range(1, n+1):
            if mp[person] == n - 1:
                return person

        return -1