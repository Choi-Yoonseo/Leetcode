class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        #count of the sum of squares
        count=0
        #length of nums
        n=len(nums) 
        for i in range(0,n) :
            if  n%(i+1)==0:
                count+=nums[i]**2
        return count