class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        f=list(range(k))
        b=[]
        c=[0]*k
        for i,a in enumerate(arrival):
            while b and b[0][0]<=a:
                _,s=heapq.heappop(b)
                bisect.insort(f,s)
            if not f:
                continue
            pos=bisect.bisect_left(f,i%k)
            if pos==len(f):
                pos=0
            s=f.pop(pos)
            c[s]+=1
            heapq.heappush(b,(a+load[i],s))
        mx=max(c)
        return [s for s in range(k) if c[s]==mx]