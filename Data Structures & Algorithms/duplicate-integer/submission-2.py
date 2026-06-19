class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return False
        seen = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] in seen:
                return True
            else: 
                seen.append(nums[i])
        return False