class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        r=[0]*len(nums)
        l=0
        for i in range(len(nums)):
            r[i]=l
            l+=nums[i]
        ri=0
        for i in range((len(nums))-1,-1,-1):
            r[i]=abs(r[i]-ri)
            ri+=nums[i]
        return r