class Solution:
    def findLHS(self, nums: List[int]) -> int:
       

        d, a = {}, 0
        for i in nums:
            if i not in d: d[i] = 1
            else: d[i] += 1
        for i in d:
            if i + 1 in d.keys():
                a = max(a, d[i] + d[i+1])
        return a