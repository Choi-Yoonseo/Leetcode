class Solution:
    def sumOfMultiples(self, n: int) -> int:
        total = 0
        for i in range(1,n+1):
            if (i%3)==0:
                total += i
            elif (i%5)==0:
                total += i
            elif (i%7)==0:
                total += i

            else:
                continue


        return total

