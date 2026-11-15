class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        mod=10**9+7
        o=0
        e=1
        c=0
        ans=0
        for num in arr:
            c+=num
            if c%2==1:
                ans=(ans+e)%mod
                o+=1
            else:
                ans=(ans+o)
                e+=1
        return ans
        