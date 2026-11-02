class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        p=0
        m=0
        for i in range(len(gain)):
            p+=gain[i]
            m=max(m,p)
        return m
        