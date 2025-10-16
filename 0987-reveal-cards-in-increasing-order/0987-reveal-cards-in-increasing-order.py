class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        n = len(deck)
        res = [0]*n
        index = deque(range(n))

        for card in deck:
            i = index.popleft()
            res[i] = card
            if index:
                index.append(index.popleft())
        return res