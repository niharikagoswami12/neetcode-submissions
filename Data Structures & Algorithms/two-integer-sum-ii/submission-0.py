class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        counter={}
        for i in range(len(numbers)):
            counter[numbers[i]]=i+1
        for i in range(len(numbers)):
            if target-numbers[i] in counter:
                return [i+1, counter[target-numbers[i]]]
        