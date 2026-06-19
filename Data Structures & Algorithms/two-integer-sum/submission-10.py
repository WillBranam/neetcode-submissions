class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        y = len(nums) -1
        temp_list = sorted([(e, i) for i, e in enumerate(nums)])
        while x < y:
            xy = temp_list[x][0] + temp_list[y][0]
            if xy == target:
                return sorted([temp_list[x][1], temp_list[y][1]])
            elif xy < target:
                x += 1
            else:
                y -= 1