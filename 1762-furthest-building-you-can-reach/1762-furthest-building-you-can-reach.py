class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = 0
        heapq = []
        brick = 0

        for i in range(len(heights)-1):
            # print('i', i, i+1, bricks)
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heappush(heapq, diff)
                if ladders:
                    # print('a')
                    ladders -= 1
                elif ladders == 0:
                    # print('b')
                    brick += heappop(heapq)
                    if brick > bricks:
                        return i
            # print(i, heapq)
        return len(heights)-1