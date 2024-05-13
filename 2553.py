class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0,len(nums)):
            if(len(str(nums[i]))> 1):
                j = str(nums[i])
                for k in j:
                    res.append(int(k))
            else:
                res.append(int(nums[i]))
        return res