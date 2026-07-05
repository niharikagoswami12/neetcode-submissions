class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        for i in range(len(numbers)):
            sum=numbers[low]+numbers[high]
            if sum == target:
                return [low+1, high+1]
            elif sum<target:
                low+=1
            elif sum>target:
                high-=1
            
            
        