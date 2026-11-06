class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        w= text.split()
        c = 0
        for word in w:
            can = True
            for ch in word:
                if ch in brokenLetters:
                    can = False
                    break
            if can:
                c += 1

        return c
        