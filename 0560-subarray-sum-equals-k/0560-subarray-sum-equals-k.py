class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = 0
        count = 0
        d = {0: 1}
        for i in range(len(nums)):
            p += nums[i]
            if p - k in d:
                count += d[p - k]
            d[p] = d.get(p, 0) + 1
        return count