class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(["#" + str(len(words)) + "#" + words for words in strs])
    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 0:
            return []
        words = []
        ptr = 0
        cur_string = ""
        cur_length = 0
        length = 0
        length_builder = ""
        length_needed = True
        while ptr != len(s):
            length_needed = True if cur_length == length else False
            if length_needed:
                cur_length = 0
                if ptr != 0:
                    words.append(cur_string)
                    cur_string = ""
                if s[ptr] == "#":
                    length, ptr = self.get_length(ptr+1, s)
                length_needed = False
            for i in range(length):
                cur_string += s[i+ptr]
                cur_length += 1
            ptr += length
        words.append(cur_string)
        return words

    def get_length(self, ptr, s) -> (int, int):
        digits = ""
        while ptr != len(s) and s[ptr] != "#":
            digits += s[ptr]
            ptr+=1
        return int(digits), ptr+1


            
