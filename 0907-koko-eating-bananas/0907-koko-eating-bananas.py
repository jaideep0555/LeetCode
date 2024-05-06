class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def cal_hours(k,l):
            res=0
            for i in l:
                res=res+ math.ceil(float(i)/k)
            return res
        # implement Binary search 
        l,r=1,max(piles)
        res=float('inf')
        while(l<=r):
            m=(l+r)//2
            x=cal_hours(m,piles)
            if(x <= h):
                res=min(res,m)
                r=m-1
            else: 
                l=m+1
        return res

