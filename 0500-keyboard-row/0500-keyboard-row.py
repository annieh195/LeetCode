class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")

        res = []
        for word in words:
            if set(word.lower()).issubset(first) or set(word.lower()).issubset(second) or set(word.lower()).issubset(third):
                res.append(word)
        return res