class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_sorted=tuple(sorted(nums))
        for i in range(1, len(nums)):
            if nums_sorted[i-1] == nums_sorted[i]:
                return True
        return False
