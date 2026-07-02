import re

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        lenMap = [(word, len(word)) for word in strs]
        encoded_str = ""
        for w, l in lenMap:
            encoded_str += str(l) + "#" + w
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        current_num = ""
        word_list = []
        i = 0
        while i < len(s):
            if s[i] in "0123456789":
                current_num += s[i]
            elif s[i] == '#':
                if current_num == "":
                    current_num = 0
                word_list.append(s[i+1: i + int(current_num)+1])
                i += int(current_num)
                current_num = ""
            i+=1
        return word_list

