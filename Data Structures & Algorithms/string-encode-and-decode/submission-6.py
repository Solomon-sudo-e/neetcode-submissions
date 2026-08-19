class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(["#" + str(len(words)) + "#" + words for words in strs])
    
    def decode(self, s: str) -> List[str]:
        words = []
        ptr = 0
        while ptr < len(s):
            ptr += 1

            end = s.find("#", ptr)

            length = int(s[ptr:end])
           
            ptr = end+1

            words.append(s[ptr:ptr+length])
            ptr += length

        return words
            



            
