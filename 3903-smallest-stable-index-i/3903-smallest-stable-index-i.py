class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            left = max(nums[0:i+1])
            right = min(nums[i:n])
            s = left - right
            if s <= k:
                return i
        return -1