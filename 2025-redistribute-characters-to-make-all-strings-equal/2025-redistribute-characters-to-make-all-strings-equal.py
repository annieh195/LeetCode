class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp = defaultdict(int)

        for word in words:
            for char in word:
                mp[char] += 1

        leng = len(words)
        for value in mp.values():
            if value % leng != 0:
                return False
        return True