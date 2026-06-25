from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for i in nums:
            if i not in freq_dict:
                freq_dict[i] = 1
            else:
                freq_dict[i] += 1
        ret_list = [0] * (len(nums) + 1)

        for key, val in freq_dict.items():
            if ret_list[val] == 0:
                ret_list[val] = []
            ret_list[val].append(key)
        i = len(ret_list) - 1
        to_ret = []
        while len(to_ret) < k:
            if ret_list[i] != 0:
                for num in ret_list[i]:
                    to_ret.append(num)
            i -= 1
        return to_ret

        