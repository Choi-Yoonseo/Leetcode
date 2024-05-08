class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        num = sorted(nums)  #정렬하기 (오름차순)
        return [num.index(i) for i in nums]