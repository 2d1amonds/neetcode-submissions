class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0, 0, 0]
        for i in range(len(nums)):
            bucket[nums[i]] += 1

        pos = 0
        for i in range(len(bucket)):
            for j in range(bucket[i]):
                nums[pos] = i
                pos += 1