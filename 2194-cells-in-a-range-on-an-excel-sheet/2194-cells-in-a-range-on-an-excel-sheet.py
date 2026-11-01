class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        s1, s2 = s.split(":")
        r = []
        for x in range(ord(s1[0]), ord(s2[0]) + 1):
            for y in range(int(s1[1]), int(s2[1]) + 1):
                r.append(chr(x) + str(y))
        return r