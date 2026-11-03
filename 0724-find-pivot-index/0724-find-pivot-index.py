class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        p=0
        l=[0]*len(nums)
        for i in range(len(nums)):
            l[i]=p
            p+=nums[i]
        s=0
        r=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            r[i]=s
            s+=nums[i]
        for i in range(len(nums)):
            if l[i]==r[i]:
                return i
        return -1


        