class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitshortner=0xffffffff

        while((b&bitshortner)>0):
            temp=(a&b)<<1
            a=a^b
            b=temp
        return (a & bitshortner) if b > 0 else a 
        