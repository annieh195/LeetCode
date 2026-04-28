class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = defaultdict(int)
        for i, string in enumerate(list1):
            count[string] = i

        res = []
        min_sum = float("inf")

        for i in range(len(list2)):
            if list2[i] in count:
                index_sum = count[list2[i]] + i

                if index_sum < min_sum:
                    min_sum = index_sum
                    res = [list2[i]]

                elif index_sum == min_sum:
                    res.append(list2[i])

        return res
