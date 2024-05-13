class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        if n== 1:
            return nums[0]
        res = sum(nums) + reduce(lambda x,y: x^y, nums)
        for i in range(2,n):
            res += sum(
                reduce(lambda x,y: x^y, item)
                for item in combinations(nums,i)
            )

        return res

        