class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        ans = R

        while L <= R:
            mid = (L + R) // 2
            total_hours = sum(self.howManyHours(pile, mid) for pile in piles)
            if total_hours <= h:
                ans = mid
                R = mid - 1
            else:
                L = mid + 1
        return ans
    
    def howManyHours(self, number: int, speed: int) -> int:
        return (number + speed - 1) // speed