class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Approach 1 using XOR
        # res=0
        # l=[x for x in range(len(nums)+1)]
        # for i in nums:
        #     res=res^i
        # for i in l:
        #     res=res^i
        # return res
        #Using Sum [0,1,2,3]- re
        res=len(nums)
        for i in range(len(nums)):
            res=res+i-nums[i]
        return res