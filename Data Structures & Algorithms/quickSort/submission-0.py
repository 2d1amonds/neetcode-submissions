# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def sort(s: int, e: int):
            if e - s <= 0:
                return
            pivot = pairs[e]
            p = s
            for i in range(s, e):
                if pairs[i].key < pivot.key:
                    pairs[p], pairs[i] = pairs[i], pairs[p]
                    p += 1
            pairs[e], pairs[p] = pairs[p], pairs[e]
            sort(s, p - 1)
            sort(p + 1, e)
        sort(0, len(pairs) - 1)
        return pairs