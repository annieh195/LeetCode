class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for symbol in "!?\',;.":
            paragraph = paragraph.replace(symbol, ' ')
        mp = defaultdict(int)
        for word in paragraph.lower().split():
            if word not in banned:
                mp[word] += 1

        maxvalue = 0
        maxkey = ""
        
        for key, value in mp.items():
            if value > maxvalue:
                maxvalue = value
                maxkey = key
        return maxkey