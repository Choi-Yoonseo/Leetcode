class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return  [[e ^ 1 for e in row[::-1]] for row in image]