class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        mp = Counter(text)
        res = len(text)
        for char in word:
            res = min(res, mp[char]//word[char])
        return res