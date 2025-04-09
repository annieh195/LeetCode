class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        l, r = 0, 1

        if len(chars) == 0:
            return 0

        if len(chars) == 1:
            return 1

        while r <= len(chars):
            if r < len(chars) and chars[l] == chars[r]:
                r += 1
            else:
                s.append(chars[l])
                if r - l > 1:
                    for c in str(r - l):
                        s.append(c)
                l = r
                r += 1

        for i in range(len(s)):
            chars[i] = s[i]

        return len(s)