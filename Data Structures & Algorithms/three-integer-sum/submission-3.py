class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        toReturn = []
        nums.sort()
        for i in range(0, len(nums), 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            low = i + 1
            high = len(nums) -1
            while low < high:
                curr_sum = nums[i] + nums[low] + nums[high]
                if curr_sum == 0:
                    toReturn.append([nums[i],nums[low],nums[high]])
                    tempLow = nums[low]
                    tempHigh = nums[high]
                    while low < high and (tempLow == nums[low] or  tempHigh == nums[high]):
                        if tempLow == nums[low]:
                            low += 1
                        if tempHigh == nums[high]:
                            high -= 1
                elif curr_sum < 0:
                    low+=1
                else:
                    high-=1
        return toReturn
            