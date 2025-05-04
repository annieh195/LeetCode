class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        n = len(deck)
        res = [0]*n
        idx = deque(range(n))

        for card in deck:
            i = idx.popleft()
            res[i] = card
            if idx:
                idx.append(idx.popleft())
        return res