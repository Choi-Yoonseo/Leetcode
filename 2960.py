class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        a=batteryPercentages
        count=0
        
        for i in a:
            if count < i:
                count=count+1
        return count

        