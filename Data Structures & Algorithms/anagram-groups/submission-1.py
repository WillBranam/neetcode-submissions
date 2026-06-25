import string
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lowercase_set = {char: 0 for char in string.ascii_lowercase}
        return_list = {}
        for word in strs:
            temp_dict = lowercase_set.copy()
            for letter in word:
                temp_dict[letter] += 1

            if tuple(temp_dict.values()) not in return_list:
                return_list[tuple(temp_dict.values())] = []

            return_list[tuple(temp_dict.values())].append(word)

        return list(return_list.values())

                
                
                