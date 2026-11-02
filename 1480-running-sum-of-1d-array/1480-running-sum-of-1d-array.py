class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        p=0
        r=[0]*(len(nums))
        for i in range(len(nums)):
            r[i]=p
            p+=nums[i]
        for i in range(len(nums)-1):
            r[i]=r[i+1]
        r[len(nums)-1]=p
        return r
