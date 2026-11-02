class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        if 0 in nums:
            result = [0] * n
            if nums.count(0) == 1:
                zero_idx = nums.index(0)
                nums.remove(0)
                result[zero_idx] = math.prod(nums)
            return result
        
        prod_nums = math.prod(nums)
        return [prod_nums // num for num in nums]
