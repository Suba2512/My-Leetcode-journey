class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        p=0
        r=[0] * (len(gain)+1)
        for i in range(len(gain)):
            r[i]=p
            p+=gain[i]
        r[len(gain)]=p
        return max(r)
        