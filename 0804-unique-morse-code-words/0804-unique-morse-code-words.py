class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        r=[]
        d={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
        for i in words:
            s=[]
            for j in i:
                s.append(d[j])
            r.append("".join(s))
        r=set(r)
        return len(r)
            
