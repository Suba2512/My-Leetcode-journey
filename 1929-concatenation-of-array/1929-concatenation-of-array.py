class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        r=[0]*(2*len(nums))
        for i in range(len(nums)):
            r[i]=nums[i]
        j=len(nums)
        for i in nums:
            r[j]=i
            j+=1
        return r
        