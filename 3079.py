class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            s = str(num)
            n = max(list(s))
            s = n*len(s)
            res += int(s)
        return res